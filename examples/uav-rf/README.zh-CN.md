[← 返回主 README](../../README.zh-CN.md) · [English Walkthrough](README.md) · **简体中文全流程样例**

# 全流程实战样例：UAV × RF 交叉文献搜调与速读

本样例完整复现 **PaperResearch**（`search` → `read` / `both`）在一轮真实跨学科文献调研中的使用流程：**系统检索并筛选 2024–2026 年“无人机（UAV）识别 × 射频（RF）感知”交叉论文，并将入选文献整理成决策优先的双语速读卡。**

> **为什么选这个案例演示？** “UAV + RF”是极易踩坑的交叉查询：关键词里混着 `NeRF` 带来的 `"RF"` 误匹配、大模型论文里的 `RADAR` 缩写、声学感知而非射频感知、以及拿“无人机机型分类”当成“个体硬件射频指纹识别（RFFI）”的边界混淆。下面的记录展示了本 skill 如何逐层排雷。

---

## 本目录包含的样例文件

| 文件 | 说明 |
| --- | --- |
| [`candidates.json`](candidates.json) | 可直接喂给 CLI 复跑的 6 篇真实候选记录（含真实 DOI 与调研释义），混合了硬件 CFO 认证、机型 RFFI、开集识别、雷达视觉定位、Remote ID 协议和 `NeRF` 误召回 |
| [`ccf-a-uav-rf.md`](ccf-a-uav-rf.md) | 2024–2026 年 CCF A 类 **19 篇 UAV × RF 交叉论文**的完整中文研究故事卡节选 |
| [`cvpr-aerial-vision.md`](cvpr-aerial-vision.md) | CVPR 2024 航空视觉先导调研 7 篇卡片节选 |
| [`cvpr-rf-sensing.md`](cvpr-rf-sensing.md) | CVPR 2024 RF 感知先导调研 12 篇卡片节选 |

---

## 第 0 步：确定研究问题与工作模式

调研最初先用 CVPR 2024–2026 主会做交互式探路（**9,629** 篇官方主会论文 → 纳入 **85** 篇：UAV 37 篇、RF 48 篇、主会直接交叉 0 篇），随后切换为 **系统盘点 / 覆盖优先模式**，扩展到 **CCF 第七版 A 类全集**（**95 个 venue**：58 个会议 + 37 个期刊，年份 2024–2026，检索截止 `2026-10-12`）。

整个过程围绕两个核心问题推进：

1. **全景盘点：** 哪些 CCF A 类正式长文属于 UAV 识别（`A`）、RF/雷达/无线感知（`B`），以及二者直接交叉（`A × B`）？
2. **决策优先筛选：** 在交叉项里，哪些论文真正评估了**硬件个体级射频指纹识别（RFFI）**（例如跨接收机、跨采集日）？哪些只是机型分类、信道/运动特征认证或空间定位？

---

## 第 1 步：`search` 问题拆解与多路召回

按 [`references/search.md`](../../references/search.md) 的流程，先把模糊主题拆解为 **“研究对象 + 输入模态 + 目标任务”**，并在大规模拉取前先立好排除护栏：

| 维度 | 纳入标准 | 明确排除 / 防误召回规则 |
| --- | --- | --- |
| **A · UAV** | UAV 作为识别/跟踪目标、UAV 作为感知平台、航空视角识别 | 纯导航避障、轨迹规划、悬停控制、三维渲染/重建 |
| **B · RF** | 物理层 RF、雷达、SAR、Wi-Fi CSI、毫米波作为主要输入或建模信号 | 纯 MAC/路由优化、纯密码学认证协议、声学 FMCW（`AGR`）、光学散射 |
| **A × B · 交叉** | UAV 识别/感知与 RF 感知**同时**参与主要任务、输入或技术贡献 | 仅在背景顺带提及；`NeRF` 中的 `"RF"`；LLM 论文里的无关 `RADAR` 缩写 |
| **出处与类型** | 2024–2026 年主会正式长文（Regular paper）与 A 类期刊 | Workshop、1–3 页 Demo、共享合集伴随 track（如 AAAI OJS 中的 `IAAI`）、勘误 |

### 多来源交叉核验与诚实缺口记录

不迷信单一搜索接口，而是把索引召回、官方目录和引文追踪对齐：

- **Semantic Scholar 索引扫描**（覆盖全部 95 个 venue）：去重后 **113,922** 条索引记录（含同名 venue 别名误召回，需进一步核验）。
- **官方主会目录采集**（CVF/CVPR、ICCV、ICLR、ICML、NeurIPS、USENIX Security、NDSS、OSDI、MobiCom、JMLR、ACM SIGOPS ATC）：**50,427** 条官方标题母表。
- **Crossref ISSN 日期窗口补检**（37 个 A 类期刊 + 5 个会议系列）+ **OpenAlex / 作者公开主页补全截断摘要**。
- **引文雪球补检**：从 4 篇交叉种子论文发出 8 次请求（3 次返回可用列表，共 86 条边 → 筛选出 **25** 条关联候选；3 次空值、2 次限流）。
- **异常不报零：** 当 DBLP 返回反机器人验证页（HTTP 200）、INFOCOM 官网返回 HTTP 418 时，显式记入覆盖缺口表，绝不把失败请求当成“该会议零论文”。

---

## 第 2 步：`search` 摘要核读筛选与漏斗对账

标题只做初步召回，**不看摘要不做纳入决定**。每条候选逐篇登记 `include`、`exclude` 或 `unresolved`（缺摘要或主会身份未确认时单列待核，绝不混入确定纳入数）：

```text
113,922 条去重索引记录 + 50,427 条官方目录标题
   │
   ▼  同义词扩展召回 + 引文雪球补检
5,884 条候选进入筛选
   ├──▶ 4,375 条排除   （3,413 条范围外/关键词陷阱、743 条非 CCF-A、60 条 workshop/demo、25 条 1–3 页短文…）
   ├──▶   507 条待核   （缺摘要或正式主会身份待核——绝不计入纳入数）
   └──▶ 1,002 篇确定纳入
           ├── 180 篇 UAV / 航空视觉识别  （2024: 39 · 2025: 74 · 2026: 67）
           ├── 803 篇 RF / 雷达与无线感知  （2024: 216 · 2025: 247 · 2026: 340）
           └──  19 篇 UAV × RF 直接交叉    （2024: 5 · 2025: 6 · 2026: 8）
```

> **先筛选、后下载：** 在确定 1,002 篇纳入清单并保存筛选快照后，才批量获取合法开放原文——最终核验通过 **344** 份 OA PDF（含复用 CVPR 先导库的 **84** 份），另有 **176** 份下载/首页校验失败、**482** 篇未检得公开地址。

### 筛选阶段实际拦截的典型陷阱

| 候选论文（出处，年份） | 陷阱类型 | 真实裁决与排除依据 |
| --- | --- | --- |
| *OSNeRF: On-demand Semantic Neural Radiance Fields...* (`ACM MM`, 2024) | 字符串子串误匹配（`NeRF` → `RF`） | **排除** — 多视角 RGB 三维语义重建，不含射频信号模态 |
| *RADAR: Redundancy-Aware Diffusion for Multi-Agent Communication...* (`ICML`, 2026) | 同名缩写撞车（`RADAR`） | **排除** — LLM 多智能体通信拓扑生成，非雷达或无线感知 |
| *AGR: Acoustic Gait Recognition Using Interpretable Micro-Range Profile* (`INFOCOM`, 2024) | 物理载体混淆（`FMCW`） | **排除** — 摘要明确载波为扬声器声学信号，不是射频雷达 |
| *CAPSID: A Private Session ID System for Small UAVs* (`CCS`, 2024) | 任务层级错位（`Remote ID`） | **排除** — 无人机广播协议层的密码学隐私标识，非物理层 RF 识别 |
| *Demo : Synthetic Data for Data-Driven Wireless* (`MobiCom`, 2024) | 会议合集混入短篇 | **排除** — 随主会合集出版的 Demo 记录，非主会正式长文 |
| *Human-in-the-Loop Eider Duck Counting...* (`AAAI` OJS, 2026) | 共享卷次子栏目（`IAAI`） | **排除** — 官方 OJS Section 为 IAAI 应用 track，非 AAAI 主会 |

---

## 第 3 步：对 19 篇 `UAV × RF` 交叉论文做决策优先排序

哪怕过了去噪这一关，这 **19 篇**交叉论文解决的也并不是同一个问题。如果下游目标是找**发射机硬件级射频指纹识别（RFFI）**，PaperResearch 会按任务粒度与评测协议把它们排好序并点出关键边界：

| 细分方向 | 篇数 | 代表论文 | PaperResearch 点明的关键判断边界 |
| --- | ---: | --- | --- |
| **1. 硬件 CFO / RFFI 认证** | **1** | *Enhanced Two-Way Privacy-Preserving PHY-Layer Auth* (`TDSC` 2025) | 最贴近个体硬件指纹（用 MOOSE 提取 CFO），**但**摘要仅报告数值仿真，缺真实跨接收机/跨天采集数据 |
| **2. 无人机类型 RF / 开集识别** | **3** | *Lightweight Memory Network* (`TIFS` 2026)、*Open-RFNet* (`JSAC` 2026)、*S3R* (`TIFS` 2024) | 识别对象是 **9–25 种无人机机型/品牌**，未验证同型号内个体区分；其中 *Open-RFNet* 重训分类层使用了未知样本 |
| **3. 信道 / 运动 / CSI 感知认证** | **4** | *Dr. Defender* (`TIFS` 2024)、*DroneMA* (`INFOCOM` 2025)、*Challenge-Response* (`TIFS` 2025)、*MmWave Sparsity* (`TIFS` 2024) | 依赖传播信道增益、CSI 螺旋桨扰动或 RSSI 运动轨迹对齐，**不等同于**发射机硬件指纹 |
| **4. 雷达跟踪、视射融合定位与 ISAC 平台** | **11** | *mmE-Loc* (`TMC` 2026)、*MIROS* (`INFOCOM` 2026)、*RFViNet* (`JSAC` 2026)、*AirGuard* (`JSAC` 2026)、*Wi2SAR* (`MobiCom` 2026) | 解决降落定位（如 0.083 m 精度）、无人机 vs. 飞鸟回波分类，或 UAV 作为无线搜救/ISAC 平台 |

### 在 [`examples/uav-rf/candidates.json`](candidates.json) 上的 `search` 输出样例

对 6 篇样例候选提问 *“筛选无人机 RF 身份识别论文，区分硬件级个体 RFFI、机型分类、空间定位和关键词陷阱”* 时，输出清单如下：

```markdown
范围与结论：已核查 6 篇候选。1 篇直接建模无人机硬件 CFO 指纹（仅数值仿真，需核实真实实验）；2 篇为无人机机型级 RF/开集识别；1 篇为降落定位任务仅作相邻参考；2 篇因属于协议隐私或 NeRF 误召回已排除。

- Enhanced Two-Way Privacy-Preserving PHY-Layer Authentication for UAV-Assisted MIMO Systems（IEEE TDSC，2025） · 10.1109/tdsc.2025.3594095 · 直接以 MOOSE 提取的 CFO 作为 UAV 硬件身份指纹并结合 ECC 认证，但摘要仅说明数值仿真，跨接收机与跨天真实表现[待核]。
- Lightweight Memory Network for Drone Type RF Fingerprint Identification in Dynamic Environments（IEEE TIFS，2026） · 10.1109/tifs.2026.3734750 · 研究动态遮挡环境下的无人机 RF 时频谱识别（95.16% 平均准确率），但数据集为 9 类无人机机型，是否包含同型号个体区分[待核]。
- Multi-Domain Supervised Contrastive Learning for UAV Radio-Frequency Open-Set Recognition（IEEE JSAC，2026） · 10.1109/jsac.2026.3669136 · 提出了多域融合与改进 OpenMax 的无人机 RF 开集识别（25 种机型闭集 95.12% / 开集 96.08%），但属于机型层级且分类层重训用到了未知样本。
- [相邻工作 / 仅定位] mmE-Loc: Facilitating Accurate Drone Landing With Ultra-High-Frequency Localization（IEEE TMC，2026） · 10.1109/tmc.2026.3666235 · 事件相机与毫米波雷达融合实现 0.083 m / 5.12 ms 降落定位，任务为空间定位而非设备身份识别。

已排除：
- CAPSID（ACM CCS，2024） · 10.1145/3658644.3690324 · Remote ID 广播隐私会话协议，无物理层 RF 感知或硬件指纹。
- OSNeRF（ACM MM，2024） · 10.1145/3664647.3681686 · 仅因 NeRF 匹配到 "RF" 子串，实为纯视觉三维重建。
```

---

## 第 4 步：`read` 依托稳定 ID 无损交接并生成速读卡

进入 `read` 阶段时，脚本或助手严格按 `paper_id` / DOI 携带筛选阶段的原始材料与出处，不会在传递中丢失摘要或编造细节。每张卡片先讲**阅读裁决与关键条件**，再展开任务、核心设计与双语摘要：

> #### Lightweight Memory Network for Drone Type RF Fingerprint Identification in Dynamic Environments
>
> - **ID / DOI：** `595d5a5d507a745e` · [`10.1109/tifs.2026.3734750`](https://doi.org/10.1109/tifs.2026.3734750) · **出处：** IEEE TIFS, 2026
> - **核读依据：** 本地来源释义摘要；摘要级速读（`https://ieeexplore.ieee.org/abstract/document/11695277/`）
>
> **一句话与阅读价值：** 该文用多尺度 spectrogram、通道/空间注意力、全局-局部双路径和可训练 memory/gate 做动态遮挡环境下的无人机 RF 识别，在 9 类数据集上报告 **95.16% 平均准确率**。值得借鉴其抗动态传播表征设计，**但引用前必须核全文实验协议**——摘要表明其评估对象是 9 种无人机类别，尚未证实能区分同型号内不同发射机个体。
>
> **任务与条件：** 输入为动态遮挡传播中的无人机 RF spectrogram，输出为 9 类无人机识别结果；含组件消融；摘要未说明跨接收机、跨采集日或同型号个体划分。
>
> **English Abstract (Paraphrase):** The paper studies drone RF fingerprint recognition under time-varying propagation and obstruction. It combines multiscale spectrogram features and channel/spatial attention with global and local feature paths, trainable memory, and gated fusion, reporting 95.16% mean accuracy across nine drone categories.
>
> **中文摘要（对应释义）：** 该文研究动态遮挡传播环境下的无人机 RF 指纹识别，结合多尺度时频谱图、通道与空间注意力、全局-局部双路径及可训练记忆门控融合，在自采 9 类无人机数据集上报告 95.16% 平均准确率；摘要尚未核实是否区分同型号内不同发射机个体。

该次调研交付的全部 **19 张交叉论文原始卡片**保存在 [`ccf-a-uav-rf.md`](ccf-a-uav-rf.md)。

---

## 第 5 步：下游研究闭环 & 本地复跑体验

在完整调研中，全部 **1,002 张双语卡片**进一步被归纳为 **8 大核心问题类别**（信号质量与身份归因 259、空间定位与成像 144、有限资源部署与协同 127、跨条件泛化与长期稳定性 121、多模态证据与缺失观测 119、隐私与对抗安全 93、低标注与开放身份空间 86、数据与评测协议 53），从而明确定位出研究空缺：**2024–2026 年 CCF A 类论文中，跨接收机/跨采集日真实数据下的硬件级 UAV 个体 RFFI 以及音视射频联合真值基准仍然高度稀缺。**

### 用 CLI 亲自复跑这个样例

配置任意 OpenAI Chat Completions 兼容端点后，仅用 Python 标准库即可在仓库根目录复现整个“筛选 → 交接 → 速读卡”流程：

```bash
export PAPER_MODEL="openai/<你的模型名>"
export PAPER_BASE_URL="https://api.openai.com/v1"
export OPENAI_API_KEY="<你的密钥>"

# 1. 先筛候选并保留原始元数据到 selected_uav_rf.json
python scripts/run.py search \
  "筛选无人机 RF 身份识别论文，区分硬件级个体 RFFI、机型分类、空间定位和关键词陷阱" \
  --input examples/uav-rf/candidates.json \
  --save-selected selected_uav_rf.json

# 2. 基于保存的清单生成决策优先双语速读卡
python scripts/run.py read \
  "开头先点明任务粒度（硬件个体 vs 机型 vs 定位）、实验划分条件和关键指标" \
  --input selected_uav_rf.json

# 或者一步串联执行 search + read：
python scripts/run.py both \
  "先挑出最相关的 3 篇无人机 RF 识别论文，再生成决策优先的双语速读卡" \
  --input examples/uav-rf/candidates.json
```
