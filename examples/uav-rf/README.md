[← Main README](../../README.md) · **English Walkthrough** · [简体中文全流程样例](README.zh-CN.md)

# End-to-End Walkthrough: UAV × RF Cross-Topic Survey

This walkthrough traces how **PaperResearch** (`search` → `read` / `both`) was used on a real cross-disciplinary literature survey: **identifying and screening 2024–2026 papers at the intersection of UAV perception/identification and Radio Frequency (RF) sensing**, then turning selected records into decision-first bilingual reading cards.

> **Why this case study matters:** Cross-disciplinary queries like *"UAV + RF"* are full of traps—papers matching `RF` inside `NeRF`, LLM frameworks named `RADAR`, acoustic sensing instead of RF, or drone *type* classifiers masquerading as *individual emitter* RF fingerprint identification (RFFI). This trace shows how PaperResearch systematically catches those traps.

---

## Included Artifacts in This Folder

| Artifact | Purpose |
| --- | --- |
| [`candidates.json`](candidates.json) | Runnable 6-paper sample (real DOIs & survey paraphrases) mixing hardware CFO auth, drone-type RFFI, open-set recognition, radar-vision localization, Remote ID privacy, and a `NeRF` false positive |
| [`ccf-a-uav-rf.md`](ccf-a-uav-rf.md) | Complete Chinese card excerpts for all **19 CCF-A UAV × RF intersection papers** (2024–2026) |
| [`cvpr-aerial-vision.md`](cvpr-aerial-vision.md) | 7 card excerpts from the CVPR 2024 aerial-vision pilot corpus |
| [`cvpr-rf-sensing.md`](cvpr-rf-sensing.md) | 12 card excerpts from the CVPR 2024 RF-sensing pilot corpus |

---

## Step 0 · Research Question & Mode Selection

The workflow began with an interactive pilot on CVPR 2024–2026 main-track proceedings (**9,629** official papers → **85** included: 37 UAV, 48 RF, 0 direct UAV × RF intersection), then scaled to **Systematic / Coverage Mode** across the full **CCF 7th Edition Category-A** venue list (**95 venues**: 58 conferences + 37 journals, years 2024–2026, cutoff `2026-10-12`).

Two downstream questions drove screening and reading priority:

1. **Broad coverage:** Which CCF-A regular papers address UAV perception (`A`), RF/radar/wireless sensing (`B`), or their true intersection (`A × B`)?
2. **Decision-first filtering:** Among `A × B` papers, which ones actually evaluate **hardware-level emitter RF fingerprint identification (RFFI)** across receivers or sessions—versus drone *type* classification, channel/mobility authentication, or spatial localization?

---

## Step 1 · `search`: Query Decomposition & Multi-Source Recall

Following [`references/search.md`](../../references/search.md), the topic was split into **Subject + Modality/Input + Task**, with explicit exclusion rules before large-scale querying:

| Dimension | Inclusion Scope | Explicit Exclusion / False-Positive Guardrails |
| --- | --- | --- |
| **A · UAV** | UAV as target (detection/ID/tracking), UAV as sensing platform, aerial-view perception | Pure navigation, trajectory planning, hover control, 3D rendering/reconstruction |
| **B · RF** | Physical-layer RF, radar, SAR, Wi-Fi CSI, mmWave as primary input or modeled signal | Pure MAC/routing optimization, cryptographic key protocols, acoustic FMCW (`AGR`), optical backscatter |
| **A × B · Intersection** | Both UAV perception/ID and RF sensing participate in the primary task/contribution | Background-only mentions; `"RF"` inside `NeRF`; unrelated acronyms like `RADAR` in LLM routing |
| **Venue & Type** | Regular/main-track conference papers and Category-A journals (2024–2026) | Workshops, 1–3 page Demos, companion tracks (e.g., `IAAI` in AAAI OJS), errata |

### Multi-Source Retrieval & Honest Gap Logging

Instead of trusting a single search endpoint, the pipeline reconciled multiple metadata sources:

- **Semantic Scholar index scan** across all 95 venues: **113,922** deduplicated index records (containing venue-alias noise requiring verification).
- **Official proceedings catalogs** (CVF/CVPR, ICCV, ICLR, ICML, NeurIPS, USENIX Security, NDSS, OSDI, MobiCom, JMLR, ACM SIGOPS ATC): **50,427** official title entries.
- **Crossref ISSN date-window queries** (37 journals + 5 conference series) + **OpenAlex / author public abstracts** to fix truncated index abstracts.
- **Citation snowballing** from 4 intersection seeds: 8 API calls (3 returned lists → 86 edges → **25** additional candidates; 3 null, 2 rate-limited).
- **Defensive failure logging:** When DBLP returned an anti-bot challenge (HTTP 200) and the INFOCOM site returned HTTP 418, those sources were recorded as **coverage gaps**, never misreported as "zero papers."

---

## Step 2 · `search`: Abstract Screening & Funnel Accounting

Titles were used *only* for candidate recall. Inclusion required reading the abstract (or verifying shared-proceedings tracks) and recording a per-item decision: `include`, `exclude`, or `unresolved` (quarantined when abstracts were missing or main-track status could not be confirmed).

```text
113,922 deduplicated index records + 50,427 official titles
   │
   ▼  Title & keyword recall (+ synonym expansion & citation snowballing)
5,884 candidates screened
   ├──▶ 4,375 excluded   (3,413 out-of-scope/keyword traps, 743 non-CCF-A, 60 workshop/demo, 25 short 1–3p, ...)
   ├──▶   507 unresolved (missing abstract or unverified main-track status — never counted as included)
   └──▶ 1,002 included
           ├── 180 UAV / Aerial Perception  (2024: 39 · 2025: 74 · 2026: 67)
           ├── 803 RF / Wireless Sensing    (2024: 216 · 2025: 247 · 2026: 340)
           └──  19 UAV × RF Intersection    (2024: 5 · 2025: 6 · 2026: 8)
```

> **Open-access PDF acquisition ran only after screening:** Of the 1,002 included records, **344** open-access PDFs were downloaded and verified (plus **84** reused from the CVPR pilot), **176** failed download/header checks, and **482** had no public OA URL.

### Real Traps Caught During Screening

| Candidate (Venue, Year) | Trap Type | Recorded Decision & Reason |
| --- | --- | --- |
| *OSNeRF: On-demand Semantic Neural Radiance Fields...* (`ACM MM`, 2024) | Substring collision (`NeRF` → `RF`) | **Excluded** — 3D vision reconstruction from multi-view RGB; zero RF signal modality |
| *RADAR: Redundancy-Aware Diffusion for Multi-Agent Communication...* (`ICML`, 2026) | Acronym collision (`RADAR`) | **Excluded** — LLM multi-agent communication topology; no radar or RF sensing |
| *AGR: Acoustic Gait Recognition Using Interpretable Micro-Range Profile* (`INFOCOM`, 2024) | Wrong physical carrier (`FMCW`) | **Excluded** — Abstract specifies speaker-emitted acoustic waves, not radio frequency |
| *CAPSID: A Private Session ID System for Small UAVs* (`CCS`, 2024) | Task mismatch (`Remote ID`) | **Excluded** — Cryptographic broadcast privacy protocol, not physical-layer RF identification |
| *Demo : Synthetic Data for Data-Driven Wireless* (`MobiCom`, 2024) | Shared-proceedings companion | **Excluded** — Demo paper bundled in conference proceedings |
| *Human-in-the-Loop Eider Duck Counting...* (`AAAI` OJS, 2026) | Shared-volume sub-track (`IAAI`) | **Excluded** — Official OJS section is IAAI Deployed Applications, not AAAI main track |

---

## Step 3 · Decision-First Ranking Across the 19 `UAV × RF` Papers

Even after filtering out noise, treating all **19** `UAV × RF` intersection papers as interchangeable would mislead a researcher looking for **emitter-level RFFI**. PaperResearch groups and ranks them by **actual task granularity and experimental protocol**:

| Sub-Group | Count | Representative Papers | Critical Boundary Flagged by PaperResearch |
| --- | ---: | --- | --- |
| **1. Hardware CFO / RFFI Authentication** | **1** | *Enhanced Two-Way Privacy-Preserving PHY-Layer Auth* (`TDSC` 2025) | Closest match (extracts MOOSE CFO hardware fingerprint), **but** evaluated via numerical simulation only—no real cross-receiver / cross-day data |
| **2. Drone-Type RF / Open-Set Recognition** | **3** | *Lightweight Memory Network* (`TIFS` 2026), *Open-RFNet* (`JSAC` 2026), *S3R* (`TIFS` 2024) | Classifies **9–25 drone types/brands**, not verified same-model individual emitters; *Open-RFNet* also retrains its classifier using unknown samples |
| **3. Channel / Mobility / CSI Detection** | **4** | *Dr. Defender* (`TIFS` 2024), *DroneMA* (`INFOCOM` 2025), *Challenge-Response* (`TIFS` 2025), *MmWave Sparsity* (`TIFS` 2024) | Relies on propagation channel gain, CSI perturbation, or RSSI mobility trend—not transmitter hardware imperfections |
| **4. Radar Tracking, Vision-Radar Fusion & UAV-as-Platform ISAC** | **11** | *mmE-Loc* (`TMC` 2026), *MIROS* (`INFOCOM` 2026), *RFViNet* (`JSAC` 2026), *AirGuard* (`JSAC` 2026), *Wi2SAR* (`MobiCom` 2026) | Spatial localization (e.g., 0.083 m landing), UAV-vs.-bird echo classification, or UAV acting as an ISAC/Wi-Fi relay platform |

### Sample `search` Output on [`examples/uav-rf/candidates.json`](candidates.json)

Running the 6-paper runnable sample against the question *"Find UAV RF emitter identification papers and separate hardware-level RFFI from type classification, localization, and keyword traps"* yields:

```markdown
Scope: 6 candidates screened for UAV hardware RF fingerprint identification (RFFI).
1 paper directly targets hardware CFO fingerprinting (simulation-only caveat); 2 target drone-type RF recognition; 1 targets RF-vision localization; 2 excluded as non-RF / protocol traps.

- Enhanced Two-Way Privacy-Preserving PHY-Layer Authentication for UAV-Assisted MIMO Systems (IEEE TDSC, 2025) · 10.1109/tdsc.2025.3594095 · Directly models CFO via MOOSE as a UAV hardware fingerprint for PHY-layer auth, though evaluation is numerical-only without cross-day/cross-receiver captures.
- Lightweight Memory Network for Drone Type RF Fingerprint Identification in Dynamic Environments (IEEE TIFS, 2026) · 10.1109/tifs.2026.3734750 · Studies dynamic-environment drone RF spectrogram recognition (95.16% mean accuracy), but abstract evaluates 9 drone categories—[pending verification] whether same-model emitter ID is tested.
- Multi-Domain Supervised Contrastive Learning for UAV Radio-Frequency Open-Set Recognition (IEEE JSAC, 2026) · 10.1109/jsac.2026.3669136 · Relevant open-set RF feature & OpenMax design (95.12% closed / 96.08% open across 25 drone types), though type-level and requires retraining classifier with unknown samples.
- [Adjacent / Localization only] mmE-Loc: Facilitating Accurate Drone Landing With Ultra-High-Frequency Localization (IEEE TMC, 2026) · 10.1109/tmc.2026.3666235 · Useful event-camera + mmWave fusion architecture (0.083 m, 5.12 ms), but solves spatial landing localization rather than emitter identity.

Excluded:
- CAPSID (ACM CCS, 2024) · 10.1145/3658644.3690324 · Remote ID cryptographic privacy protocol; no physical-layer RF sensing.
- OSNeRF (ACM MM, 2024) · 10.1145/3664647.3681686 · "RF" matched inside NeRF; RGB 3D reconstruction only.
```

---

## Step 4 · `read`: Deterministic ID Handoff & Decision-First Card

Selected items carry their exact `paper_id`, DOI, venue, year, and verified source text directly into `read`. Each card puts **the decision-making verdict and evidence conditions first**, followed by the bilingual abstract/paraphrase and provenance:

> #### Lightweight Memory Network for Drone Type RF Fingerprint Identification in Dynamic Environments
>
> - **ID / DOI:** `595d5a5d507a745e` · `10.1109/tifs.2026.3734750` · **Venue:** IEEE TIFS, 2026
> - **Evidence Basis:** Abstract-level screening (`source-grounded paraphrase`; publisher URL verified)
>
> **Bottom Line & Why Read:** Proposes a compact multiscale spectrogram + attention + trainable memory-gate network for dynamic obstructed RF propagation, reporting **95.16% mean accuracy on a 9-category drone dataset**. Worth reading for temporal/occlusion feature stabilization, **but check full text before citing as individual RFFI**—the abstract evaluates 9 drone categories rather than same-model hardware transmitters.
>
> **Task & Conditions:** Input: drone RF spectrograms under time-varying obstruction → Output: 9 drone classes; includes component ablations; cross-receiver / cross-day and intra-model emitter splits are unverified at abstract level.
>
> **English Abstract (Paraphrase):** The paper studies drone RF fingerprint recognition under time-varying propagation and obstruction. It combines multiscale spectrogram features and channel/spatial attention with global and local feature paths, trainable memory, and gated fusion, reporting 95.16% mean accuracy across nine drone categories.
>
> **中文摘要（对应释义）：** 该文研究动态遮挡传播环境下的无人机 RF 指纹识别，结合多尺度时频谱图、通道与空间注意力、全局-局部双路径及可训练记忆门控融合，在自采 9 类无人机数据集上报告 95.16% 平均准确率；摘要尚未核实是否区分同型号内不同发射机个体。

See all **19** original Chinese cards from this survey in [`ccf-a-uav-rf.md`](ccf-a-uav-rf.md).

---

## Step 5 · Downstream Payoff & Reproducing Locally

In the full survey, all **1,002** reading cards were tagged into an **8-category primary problem taxonomy** (*Signal Quality & Attribution*: 259, *Spatial Localization & Imaging*: 144, *Resource-Constrained Deployment*: 127, *Cross-Condition Generalization*: 121, *Multimodal Evidence*: 119, *Privacy & Adversarial Security*: 93, *Low-Label & Open-Set*: 86, *Datasets & Evaluation*: 53). This exposed the exact gap: **real-world cross-receiver / cross-day hardware-level UAV RFFI and synchronized RF-vision ground truth remain largely unaddressed across CCF-A 2024–2026.**

### Try This Sample Yourself

Run the screening and card-generation pipeline locally against [`examples/uav-rf/candidates.json`](candidates.json) using any OpenAI-compatible endpoint (only Python standard library needed):

```bash
export PAPER_MODEL="openai/<your-model>"
export PAPER_BASE_URL="https://api.openai.com/v1"
export OPENAI_API_KEY="<your-key>"

# 1. Screen candidates and save selected records with original metadata
python scripts/run.py search \
  "Find UAV RF identification papers and distinguish hardware emitter RFFI from drone-type classification, localization, and keyword traps" \
  --input examples/uav-rf/candidates.json \
  --save-selected selected_uav_rf.json

# 2. Generate decision-first bilingual reading cards from the saved shortlist
python scripts/run.py read \
  "Lead with task granularity (hardware emitter vs drone type vs localization), split conditions, and reported metrics" \
  --input selected_uav_rf.json

# Or chain both steps in a single run:
python scripts/run.py both \
  "Select the top 3 UAV RF identification papers and generate decision-first bilingual reading cards" \
  --input examples/uav-rf/candidates.json
```
