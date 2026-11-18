"""Run either stage against a text-generation API."""
import argparse
import html
import json
import os
from pathlib import Path
import re
import sys
from urllib.parse import urlencode
from urllib.request import Request, urlopen

REFS = Path(__file__).resolve().parents[1] / "references"


def candidates(query, limit):
    params = urlencode({"query.bibliographic": query, "rows": limit})
    with urlopen("https://api.crossref.org/works?" + params, timeout=40) as response:
        items = json.load(response)["message"]["items"]
    records = []
    for item in items:
        if not item.get("title") or not item.get("DOI"):
            continue
        date = item.get("published", {}).get("date-parts", [[]])[0]
        records.append(dict(paper_id=item["DOI"], title=item["title"][0],
                            venue=next(iter(item.get("container-title", [])), ""),
                            year=date[0] if date else None, source="Crossref",
                            abstract=html.unescape(re.sub("<[^>]+>", " ", item.get("abstract", "")))))
    return records


def complete(args, stage, task, material):
    instructions = (REFS / (stage + ".md")).read_text(encoding="utf-8")
    prompt = f"{instructions}\n\n研究问题：{args.topic}\n{task}\n以下为来源材料：\n{material}"
    messages = [{"role": "user", "content": prompt}]
    if args.base_url and args.model.startswith("openai/"):
        headers = {"Content-Type": "application/json"}
        if os.getenv("OPENAI_API_KEY"):
            headers["Authorization"] = "Bearer " + os.environ["OPENAI_API_KEY"]
        body = {"model": args.model.split("/", 1)[1], "messages": messages}
        request = Request(args.base_url.rstrip("/") + "/chat/completions",
                          data=json.dumps(body).encode(), headers=headers)
        with urlopen(request, timeout=180) as response:
            content = json.load(response)["choices"][0]["message"]["content"]
    else:
        from litellm import completion
        options = {"api_base": args.base_url} if args.base_url else {}
        reply = completion(model=args.model, messages=messages, **options)
        content = reply.choices[0].message.content
    if not isinstance(content, str) or not content.strip():
        raise ValueError("模型未返回文本")
    return content.strip()


def screen(args, records):
    by_id = {record["paper_id"]: record for record in records}
    task = ('从以下候选中按阅读价值选取符合要求的论文，缺证据的线索在理由中标明待核。'
            '仅输出 JSON 对象，summary 是范围与结论，papers 是排序后的数组，'
            '每项含原样的 paper_id 和一句 reason。没有合适论文时给空数组。')
    if not by_id:
        return "本次检索未返回候选。", []
    raw = complete(args, "search", task, json.dumps(list(by_id.values()), ensure_ascii=False))
    payload = json.loads(re.sub(r"^\x60{3}(?:json)?\s*|\s*\x60{3}$", "", raw, flags=re.I))
    chosen = []
    lines = [payload["summary"]]
    for selection in payload["papers"]:
        paper_id = selection["paper_id"]
        if paper_id not in by_id:
            raise ValueError("筛选结果包含未知或重复标识：" + str(paper_id))
        record = by_id.pop(paper_id)
        chosen.append(record)
        lines.append(f"- {record['title']}（{record.get('venue') or 'venue 待核'}，"
                     f"{record.get('year') or '年份待核'}） · {paper_id} · {selection['reason']}")
    return "\n".join(lines), chosen


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["search", "read", "both"])
    parser.add_argument("topic", help="研究问题和取舍要求")
    parser.add_argument("--model", default=os.getenv("PAPER_MODEL"))
    parser.add_argument("--base-url", default=os.getenv("PAPER_BASE_URL"))
    parser.add_argument("--query", help="发给 Crossref 的领域检索词")
    parser.add_argument("--limit", type=int, default=20, choices=range(1, 101), metavar="1..100")
    parser.add_argument("--input", type=Path, help="候选 JSON 数组，或 read 模式的阅读材料")
    parser.add_argument("--save-selected", type=Path, help="保存筛选后的 JSON，供 read 复用")
    args = parser.parse_args()
    if not args.model:
        parser.error("请指定 --model 或 PAPER_MODEL")
    if args.mode == "read" and (not args.input or args.save_selected):
        parser.error("read 需要 --input，且不使用 --save-selected")
    supplied = args.input.read_text(encoding="utf-8") if args.input else None
    if args.mode == "read" and args.input.suffix.lower() != ".json":
        chunks = [supplied]
    else:
        records = json.loads(supplied) if supplied is not None else candidates(args.query or args.topic, args.limit)
        if not isinstance(records, list) or not all(isinstance(r, dict) and
                isinstance(r.get("paper_id"), str) and r["paper_id"] and r.get("title") for r in records):
            raise ValueError("JSON 应为论文数组，每项需要 paper_id 字符串和 title")
        if args.mode != "read":
            summary, records = screen(args, records)
            print(summary, flush=True)
            if args.save_selected:
                args.save_selected.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
            if args.mode == "search":
                return
        chunks = [json.dumps(r, ensure_ascii=False) for r in records]
    for chunk in chunks:
        if not chunk.strip():
            raise ValueError("阅读材料为空")
        print("\n" + complete(args, "read", "依据给定材料直接生成阅读卡。", chunk), flush=True)


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, OSError, ImportError) as error:
        sys.exit(f"运行失败：{error}")
