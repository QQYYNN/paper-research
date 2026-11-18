<div align="center">

# PaperResearch

**English** · [简体中文](README.zh-CN.md)

[![Agent Skill](https://img.shields.io/badge/Agent_Skill-SKILL.md-2563eb)](#option-1-use-as-an-ai-agent-skill)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776ab)](#option-2-standalone-python-cli--llm-apis)
[![OpenAI & LiteLLM](https://img.shields.io/badge/LLM-OpenAI_Compatible_%7C_LiteLLM-10a37f)](#option-2-standalone-python-cli--llm-apis)
[![CI](https://img.shields.io/badge/CI-unittest-16a34a)](.github/workflows/ci.yml)

**Turn a research question into an evidence-ranked shortlist, then turn selected papers into decision-first bilingual reading cards.**

</div>

PaperResearch is a general-purpose **Agent Skill** and **provider-agnostic CLI workflow** for academic literature discovery and rapid reading. Use `search` to filter noisy candidates, `read` to generate structured evidence-first Markdown cards from abstracts or PDFs, or chain both in one pass (`both`).

---

## Why PaperResearch?

Standard paper searches return piles of keyword matches, and generic LLM summaries often hide the exact details that decide whether a paper actually applies to your work.

| Common Pain Point | How PaperResearch Solves It |
| --- | --- |
| **Keyword & venue traps** <br/>Queries pull in substring accidents (e.g., `NeRF` matching `RF`), unrelated method acronyms, workshops, or 2-page demos. | **Subject + Modality + Task decomposition** <br/>Separates target, input modality, and task before querying; deduplicates by DOI/official record; quarantines thin records as `pending verification`. |
| **Summaries hide deal-breakers** <br/>"Achieves 95% accuracy" sounds great until you read the PDF and discover a random split, toy simulation, or mismatched task granularity. | **Decision-first reading cards** <br/>Leads every card with *what was done, decisive evidence, and boundary conditions* (dataset, split, metric, source basis) before full summaries. |
| **Context drift & hallucinations** <br/>Multi-turn chats drop DOIs/abstracts between discovery and reading, or extrapolate abstracts into invented model details. | **Deterministic `paper_id` / DOI handoff** <br/>Carries original metadata, abstracts, and source provenance from `search` into `read` via JSON (`--save-selected`), flagging gaps instead of guessing. |
| **Heavyweight audit tax on Day 1** <br/>Exhaustive survey protocols slow down quick exploration when you just want 5 high-signal papers to start reading. | **Scale-adaptive rigor** <br/>Delivers an actionable shortlist immediately by default; triggers full catalog audits, exclusion logs, and coverage gap reporting only when you ask for counts or research-gap claims. |

---

## Core Modes & Architecture

Run each stage independently or chain them end-to-end:

| Mode | Best For | Input | Output |
| --- | --- | --- | --- |
| **`search`** | *"Which papers should I read first?"* | Research question + Crossref query or candidate JSON | Ranked shortlist with one-line inclusion rationales, DOIs, `pending` flags, and optional `selected.json` |
| **`read`** | *"What did these papers actually prove?"* | Selected JSON, abstracts, Markdown notes, or extracted PDF text | Decision-first Markdown cards with key evidence, bilingual (EN/ZH) abstracts or paraphrases, and provenance |
| **`both`** | *"Find the best papers and summarize them now."* | Research question + Crossref query or candidate JSON | Screened shortlist + matching reading cards built from the preserved original records |

```mermaid
flowchart LR
    Q["Research Question<br/>or Existing Bibliography"] --> M{"Entry Mode"}
    M -->|"search / both"| S1["Decompose Query:<br/>Subject · Modality · Task"]
    S1 --> S2["Collect & Deduplicate<br/>(Crossref / Official Lists / JSON)"]
    S2 --> S3["Screen Abstracts<br/>(Include · Exclude · Pending)"]
    S3 -->|"search"| OUT1["Ranked Shortlist<br/>+ Save selected.json"]
    S3 -->|"both"| R1
    M -->|"read"| R1["Load Preserved Records<br/>(JSON / Markdown / Text)"]
    R1 --> R2["Decision-First Takeaway:<br/>Evidence · Splits · Caveats"]
    R2 --> R3["Bilingual Abstract (EN/ZH)<br/>+ On-Demand Deep Dive"]
    R3 --> OUT2["Markdown Reading Cards"]
```

---

## Quickstart

### Option 1: Use as an AI Agent Skill

Install the skill files (`SKILL.md` + `references/`) into your coding or research agent's skills directory:

```bash
# Example: copy or symlink into Codex, Claude Code, or project-local skills
cp -r path/to/paper-research ~/.codex/skills/paper-research
# or for Claude Code:
cp -r path/to/paper-research ~/.claude/skills/paper-research
```

Then ask your assistant in natural language (English or Chinese):

- **Discover & screen (`search`):**
  > Use `paper-research` to find the 5 papers most relevant to cross-day domain generalization in wearable sensing. Rank them by direct experimental evidence and give one inclusion rationale each.
- **Read existing papers (`read`):**
  > Use `paper-research` in `read` mode on these abstracts/PDFs. Lead each card with the task definition, evaluation splits, and key numbers, followed by bilingual abstracts.
- **End-to-end (`both`):**
  > Find 3 top-venue papers on event-camera + radar fusion for small-target tracking, screen out simulation-only works, and build decision-first bilingual reading cards.

### Option 2: Standalone Python CLI & LLM APIs

Works with **any OpenAI Chat Completions-compatible endpoint** using **Python's standard library only** (no third-party packages required), or with OpenAI / Anthropic / Gemini / local models via **LiteLLM**.

#### A. OpenAI-Compatible Endpoint (Zero Dependencies)

Supports OpenAI API, proxies, vLLM, Ollama, DeepSeek, Qwen, and OneAPI:

```bash
export PAPER_MODEL="openai/<deployment-or-model-name>"
export PAPER_BASE_URL="https://api.openai.com/v1"   # include /v1 if required
export OPENAI_API_KEY="<your-api-key>"

# Quick offline test using the bundled synthetic fixture:
python scripts/run.py search "Find candidates that evaluate generalization across recording days" \
  --input examples/candidates.json \
  --save-selected papers.json

python scripts/run.py read "Build bilingual cards focused on task definitions and evaluation splits" \
  --input papers.json
```

#### B. Multi-Provider via LiteLLM

```bash
python -m pip install litellm
export PAPER_MODEL="anthropic/claude-sonnet-4-20250514"   # or gemini/..., openai/...
export ANTHROPIC_API_KEY="<your-api-key>"

# Live discovery from Crossref (omit --input and provide --query):
python scripts/run.py both "Find recent papers on open-set RF device recognition" \
  --query "open-set radio frequency fingerprint identification" \
  --limit 20 \
  --save-selected selected.json > cards.md
```

> **Note:** Built-in live search fetches up to `--limit` (default `20`, max `100`) bibliographic records from Crossref for fast discovery. For exhaustive venue surveys, supply official proceedings/index JSON arrays via `--input`. See [API Reference](references/api.md) for JSON schema details and prompt-only SDK integration.

### Option 3: Prompt Templates Only (Any Language / SDK)

Read [`references/search.md`](references/search.md) or [`references/read.md`](references/read.md) as UTF-8 strings and combine them with your research question and source text in any custom LLM pipeline—no tool calling or agent harness required.

---

## Real-World Showcase: UAV × RF Cross-Topic Survey

To demonstrate how the workflow handles **noisy terminology, strict task boundaries, and scale-up surveys**, we preserve a complete real-world trace from a cross-venue survey on **UAV identification × Radio Frequency (RF) sensing (CCF Category-A, 2024–2026)**.

1. **Multi-source recall & official verification:** Combined Semantic Scholar (`113,922` index records) with official proceedings title lists (`50,427` titles across CVPR, ICLR, ICML, NeurIPS, USENIX, NDSS, MobiCom, etc.), Crossref, OpenAlex, and 4-seed citation snowballing across **95 CCF-A venues** (58 conferences + 37 journals), logging unreachable/anti-bot sources honestly as coverage gaps.
2. **Noise & trap filtering (`5,884` candidates → `1,002` included / `4,375` excluded / `507` unresolved):** Caught substring accidents (`OSNeRF` matching `RF` inside `NeRF`), acronym collisions (`RADAR` in LLM multi-agent papers), wrong physical carriers (`AGR` acoustic FMCW), protocol-only privacy (`CAPSID` Remote ID), and shared-volume tracks (`IAAI` inside AAAI OJS; 1–3 page Demos/Workshops).
3. **Decision-first granularity separation on the `19` `UAV × RF` intersections:** Prevented conflating **hardware CFO/RFFI auth (1)**, **drone-type RF / open-set classification (3)**, **channel/mobility/CSI detection (4)**, and **vision-radar localization / radar tracking / ISAC platforms (11)**.
4. **Scale-up synthesis:** Produced **1,002 bilingual abstract-level reading cards** tagged into an **8-category problem taxonomy** to pinpoint genuine research gaps.

<details>
<summary><strong>Preview: Sample Screening Output & Reading Card from the UAV × RF Showcase</strong></summary>

**Input:** [`examples/uav-rf/candidates.json`](examples/uav-rf/candidates.json) (6 real records mixing hardware CFO auth, drone-type RFFI, open-set recognition, radar-vision localization, Remote ID privacy, and a `NeRF` false positive).

**1. `search` Screening Output (Decision-First Ranking + Trap Filtering):**

```markdown
Scope: 6 candidates screened for UAV hardware RF fingerprint identification (RFFI).
1 paper models hardware CFO (simulation-only caveat); 2 evaluate drone-type RF recognition; 1 targets localization; 2 excluded as protocol/keyword traps.

- Enhanced Two-Way Privacy-Preserving PHY-Layer Authentication for UAV-Assisted MIMO Systems (IEEE TDSC, 2025) · 10.1109/tdsc.2025.3594095 · Extracts MOOSE CFO as a hardware UAV fingerprint, though evaluation is numerical simulation without cross-day/cross-receiver captures.
- Lightweight Memory Network for Drone Type RF Fingerprint Identification in Dynamic Environments (IEEE TIFS, 2026) · 10.1109/tifs.2026.3734750 · Reports 95.16% accuracy under time-varying obstruction, but evaluates 9 drone categories—[pending verification] whether same-model emitters are separated.
- Multi-Domain Supervised Contrastive Learning for UAV Radio-Frequency Open-Set Recognition (IEEE JSAC, 2026) · 10.1109/jsac.2026.3669136 · Reports 95.12% closed / 96.08% open-set accuracy across 25 drone types; type-level and retrains classifier using unknown samples.
- [Adjacent / Localization] mmE-Loc: Facilitating Accurate Drone Landing With Ultra-High-Frequency Localization (IEEE TMC, 2026) · 10.1109/tmc.2026.3666235 · Fuses event camera + mmWave radar for 0.083 m landing localization, not emitter identity.

Excluded:
- CAPSID (ACM CCS, 2024) · 10.1145/3658644.3690324 · Remote ID cryptographic privacy protocol; no physical-layer RF sensing.
- OSNeRF (ACM MM, 2024) · 10.1145/3664647.3681686 · "RF" matched inside NeRF; RGB 3D reconstruction only.
```

**2. `read` Card Output (Excerpt):**

> **Lightweight Memory Network for Drone Type RF Fingerprint Identification in Dynamic Environments** · IEEE TIFS, 2026 · `10.1109/tifs.2026.3734750`
>
> **Why Read & Boundary:** Proposes multiscale spectrograms + attention + trainable memory-gate fusion under dynamic obstructed propagation (**95.16% mean accuracy across 9 drone categories**). Valuable for anti-drift feature stabilization, **but verify full text before treating as emitter-level RFFI** (abstract establishes category-level rather than intra-model device separation).
>
> **English Abstract (Paraphrase):** Studies drone RF fingerprint recognition under time-varying propagation and obstruction using multiscale spectrograms, dual global/local attention paths, and gated memory fusion on a 9-category dataset (95.16% mean accuracy).
>
> **中文摘要（对应释义）：** 研究动态遮挡传播下的无人机 RF 指纹识别，结合多尺度频谱、注意力与可训练记忆门控融合，在 9 类无人机数据集上取得 95.16% 平均准确率；是否区分同型号个体需核查全文实验协议。

</details>

- [**Full Step-by-Step UAV × RF Walkthrough (EN)**](examples/uav-rf/README.md) · [**全流程中文样例 (ZH)**](examples/uav-rf/README.zh-CN.md)
- [**19 UAV × RF Intersection Cards (Excerpt)**](examples/uav-rf/ccf-a-uav-rf.md) · [**Runnable 6-Paper JSON**](examples/uav-rf/candidates.json)
- [**CVPR 2024 Pilot Excerpts:**](examples/uav-rf/cvpr-aerial-vision.md) [Aerial Vision (7 cards)](examples/uav-rf/cvpr-aerial-vision.md) · [RF Sensing (12 cards)](examples/uav-rf/cvpr-rf-sensing.md)

---

## Repository Structure

```text
paper-research/
├── SKILL.md                        # Agent Skill entrypoint (intent routing for search / read / both)
├── references/
│   ├── search.md                   # Screening instructions & coverage-expansion rules
│   ├── read.md                     # Decision-first bilingual reading card instructions
│   └── api.md                      # CLI flags, JSON schema, and multi-provider setup
├── scripts/
│   └── run.py                      # Provider-agnostic CLI (Crossref + OpenAI stdlib / LiteLLM)
├── examples/
│   ├── candidates.json             # Minimal synthetic 2-paper fixture for smoke testing
│   └── uav-rf/                     # End-to-end UAV × RF showcase, JSON sample, and real card excerpts
├── tests/
│   └── test_cli.py                 # Unit tests verifying search / read / both handoff via mock HTTP server
└── .github/workflows/ci.yml        # GitHub Actions CI running CLI tests on Python 3.12
```

> **Language note:** The core agent prompts in [`SKILL.md`](SKILL.md) and [`references/`](references/search.md) are authored in Simplified Chinese and work reliably across English and Chinese literature; the `read` stage is designed to produce bilingual (English + Chinese) cards.

---

## Testing & Verification

Run the unit test suite locally (uses an in-process mock OpenAI endpoint, no network or API key needed):

```bash
python -m unittest discover -s tests -v
```

GitHub Actions automatically runs this suite on every push and pull request ([`.github/workflows/ci.yml`](.github/workflows/ci.yml)).
