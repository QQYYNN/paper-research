# API 与命令行

在项目根目录运行以下命令。原生供应商接口可在 Python 虚拟环境安装 LiteLLM 后使用。已有 OpenAI Chat Completions 兼容端点时，只需 Python 标准库：设置 PAPER_MODEL=openai/实际部署名、PAPER_BASE_URL（含服务要求的 /v1 等前缀）和该服务的 OPENAI_API_KEY。脚本调用普通文本生成接口，文献检索由宿主完成。研究题目和本次输入材料会发送给所选模型。

~~~bash
python -m pip install litellm
# 使用与你的账户匹配的模型标识和供应商环境变量，例如：
# PAPER_MODEL=openai/<模型名>       OPENAI_API_KEY
# PAPER_MODEL=anthropic/<模型名>    ANTHROPIC_API_KEY
# PAPER_MODEL=gemini/<模型名>       GEMINI_API_KEY
# 自建 OpenAI 兼容服务使用 openai/<部署名> 与 PAPER_BASE_URL
# 先在 shell 中 export 对应变量，然后运行：

python scripts/run.py search '找能评估跨采集日泛化的无人机个体识别论文' \
  --query 'UAV radio frequency fingerprint identification cross session' --save-selected papers.json
python scripts/run.py read '关注跨天评测和标签定义' --input papers.json
python scripts/run.py both '先挑三篇最相关的，再做速读卡' --input candidates.json
~~~

search 和 both 缺省从 Crossref 获取前 20 项候选，可用 --limit 调整。这是单来源的快速发现入口。需要指定会议全集或穷举时，由宿主先从正式目录采集候选，带摘要传入 --input。JSON 输入是数组，每项至少有字符串 paper_id 和 title，建议提供 venue、year、abstract、source，有正文时可加 text。--save-selected 保存所选原始记录，供另一天或另一个模型继续读。标准输出是阅读用 Markdown，可重定向到文件。read 也接受 UTF-8 的 Markdown 或纯文本；PDF 由宿主先提取文本。JSON 按篇调用，单篇或单个文本文件应能放入目标模型上下文。

已有其他语言或模型 SDK 的项目可以直接读取 search.md 或 read.md 的 UTF-8 文本，把所选步骤、研究问题和来源材料合成一条用户消息发给自己的 API。两步串联时按第一步返回的稳定标识取回原始材料，再送入第二步。这样无需依赖供应商的文件读取、联网或函数调用能力。模型路由及认证参数见 [LiteLLM 文档](https://docs.litellm.ai/docs/)，内置书目来源见 [Crossref REST API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/)。
