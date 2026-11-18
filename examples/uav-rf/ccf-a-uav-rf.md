[English README](../../README.md) · [中文 README](../../README.zh-CN.md) · [Walkthrough (EN)](README.md) · [全流程样例 (中文)](README.zh-CN.md)

# CCF A 2024–2026 · UAV × RF 交叉 / Intersection

节选自历史调研文档 `paper-story-cards.md`。保留选中段落的原有卡片文字、编号和顺序。出版社摘要、摘要译文、本地文件路径和内部项目笔记经删节，论文链接可用于查阅原摘要。

Excerpt from the original `paper-story-cards.md` in the survey archive. Card notes, numbering, and order are preserved in Chinese. Publisher abstracts, their translations, local paths, and internal project notes are omitted. Follow the paper links for the abstracts.

## UAV × RF 交叉

### 2024（5 篇）

#### 1. Classification of Small Drones Using Low-Uncertainty Micro-Doppler Signature Images and Ultra-Lightweight Convolutional Neural Network

- ID：`3968514061c0128e`
- 作者：Junhyeong Park; Jun-Sung Park
- 发表：TIP，2024；正式卷期/出版登记
- Scope：雷达无人机跟踪/类型分类
- 核读依据：本地保存摘要；摘要级速读。
- 摘要来源：`https://openalex.org/W4394951249`
- DOI：[`10.1109/tip.2024.3388895`](https://doi.org/10.1109/tip.2024.3388895)
- 主要问题：效率与边缘部署；次要问题：信号质量与可观测性

**TL;DR 一句话：** 该文通过改进 FMCW 雷达 MDS 图像生成并配合 ultra-lightweight CNN，实现小型无人机远距离实时分类，在保持高准确率的同时显著降低计算量。

**任务：** 输入对象是 FMCW 雷达生成的小型无人机 micro-Doppler signature 图像；输出对象是小型无人机类别；已知协议为雷达 MDS 图像分类，评估图像质量、uncertainty quantification、分类准确率以及模型参数量/节点数/FLOPs。

**Argue 点：** 作者希望证明：提升 MDS 图像质量可以降低分类不确定性并提高 CNN 分类准确率，而专门设计的 ultra-lightweight CNN 能在远距离小型无人机实时分类中同时满足高效率和高准确性。

**核心创新：**

- 提出 MDS 图像生成技术，用于提升 FMCW 雷达 micro-Doppler signature 图像质量，从输入可观测性层面增强分类。
- 设计 ultra-lightweight CNN，在极低参数量和计算量条件下保持小型无人机分类准确性能。
- 引入 uncertainty quantification 作为图像质量改进有效性的验证手段。

**解决的问题／故事：** 小型无人机带来安全威胁，雷达微多普勒图像可用于分类，但实时部署要求图像质量高且模型足够轻。现有 CNN 方法可能受 MDS 图像质量和计算成本限制。该文同时改进 MDS 图像生成和轻量 CNN，摘要报告最高 100%、平均 99.21% 分类准确率，以及约 4.88 K 参数、21.51 K 节点、31.52 M FLOPs；但它识别的是无人机类型/类别，不是发射机硬件个体 RFFI。

---

#### 2. Dr. Defender: Proactive Detection of Autopilot Drones Based on CSI

- ID：`aae540115d11130f`
- 作者：Jiangyi Deng; Xiaoyu Ji; Beibei Wang; Bin Wang; Wen-Yuan Xu
- 发表：TIFS，2024；正式卷期/出版登记
- Scope：UAV × RF 感知/识别
- 核读依据：本地保存摘要；摘要级速读。
- 摘要来源：`https://openalex.org/W4386432037`
- DOI：[`10.1109/tifs.2023.3311964`](https://doi.org/10.1109/tifs.2023.3311964)
- 主要问题：信号质量与可观测性；次要问题：空间定位跟踪与成像

**TL;DR 一句话：** Dr. Defender 利用环境 Wi-Fi CSI 主动感知无人机螺旋桨运动，在无人机自动驾驶且无控制 RF 信号时仍可检测 10 米外无人机。

**任务：** 输入对象是家庭 Wi-Fi 信号的 CSI 以及无人机引起的信道扰动；输出对象是自动驾驶无人机是否存在的检测结果；已知协议是不要求无人机或控制器主动发射检测信号，在无人机相对窗户的不同距离和方向下评估。

**Argue 点：** 作者希望证明：即使自动驾驶无人机不发射控制通信信号，环境 Wi-Fi CSI 仍能捕捉其螺旋桨和机体运动特征，从而支持主动、非协作的室内/窗边无人机检测。

**核心创新：**

- 提出 Dr. Defender 主动检测系统，用家庭既有 Wi-Fi 信号替代被动监听无人机-控制器 RF 通信。
- 将无人机螺旋桨 shifting、moving、spinning 等运动特征映射到 Wi-Fi CSI 物理层变化，用于检测无发射自动驾驶无人机。
- 实现无需无人机或控制器发送信号的 CSI-based proactive drone detection，并在不同距离和方向条件下验证。

**解决的问题／故事：** 带摄像头消费无人机可能侵犯隐私，但自动驾驶模式下没有控制器通信信号，传统被动 RF 检测会失效。该文转向利用住宅中已有 Wi-Fi 信号，把无人机运动对 CSI 的扰动作为检测依据。摘要证据显示 Dr. Defender 在不同距离和方向下验证，并可准确检测 10 米外无人机；但摘要未提供具体准确率、误报率或跨环境泛化结果。

---

#### 3. Open Set Learning for RF-Based Drone Recognition via Signal Semantics

- ID：`7546f27bbf3c9391`
- 作者：Ningning Yu; Jiajun Wu; Cheng-Wei Zhou; Zhi-Guo Shi; Ji-Ming Chen
- 发表：TIFS，2024；正式卷期/出版登记
- Scope：RF 无人机开放集识别
- 核读依据：本地保存摘要；摘要级速读。
- 摘要来源：`https://openalex.org/W4402673895`
- DOI：[`10.1109/tifs.2024.3463535`](https://doi.org/10.1109/tifs.2024.3463535)
- 主要问题：未知目标与可靠拒识；次要问题：数据集与评测协议、信号质量与可观测性

**TL;DR 一句话：** S3R 将 RF 无人机频谱分解为纹理与位置语义，用离群阈值做开集未知检测并对未知样本聚类细分，解决闭集 RF 无人机识别误收未知类的问题。

**任务：** 输入对象是 RF 无人机信号经 STFT 构建的频谱；输出对象包括已知无人机类别、未知实例检测结果以及未知实例聚类后的具体类别；已知协议为闭集与开集识别，真实世界 spectrogram 数据集 含 24 类、7 个品牌。

**Argue 点：** 作者希望证明：通过构建结构化 signal semantics，并用每个已知类的离群点确定开集边界，可以同时提升 RF 无人机闭集识别、未知检测和未知类细分的准确率与泛化性。

**核心创新：**

- 提出 Signal Semantic-based open Set Recognition（S3R），将 STFT 频谱中的纹理特征和位置特征融合并结构优化为可区分 signal semantics。
- 设计 outlier analysis-based semantic classifier，用闭集中每个已知类别的离群点作为边界阈值来检测未知实例。
- 在增强语义空间中对检测到的未知实例进行 clustering，并发布包含 24 类、7 品牌的真实世界无人机 spectrogram 数据集。

**解决的问题／故事：** RF 无人机识别在公共安全中需要面对未见过的无人机信号，但闭集模型会把未知信号误判为已知类别。S3R 用频谱语义建立已知类边界，并把未知检测与未知类聚类连接起来。摘要称其在闭集和开集准确率、泛化性上优于 SOTA，并发布 24 类 7 品牌数据集；但摘要未说明是否识别同型号硬件个体，也未给出跨接收机/日期评测。

---

#### 4. PHY-Layer Authentication Exploiting Channel Sparsity in MmWave MIMO UAV-Ground Systems

- ID：`6697766589514b6d`
- 作者：Yu-Lin Teng; Pin-Chang Zhang; Xiao Chen; Xiao-Hong Jiang; Fu Xiao
- 发表：TIFS，2024；正式卷期/出版登记
- Scope：UAV 链路信道认证；非硬件 RFFI
- 核读依据：本地保存摘要；摘要级速读。
- 摘要来源：`https://openalex.org/W4393372418`
- DOI：[`10.1109/tifs.2024.3384112`](https://doi.org/10.1109/tifs.2024.3384112)
- 主要问题：感知通信协同设计；次要问题：空间定位跟踪与成像、信号质量与可观测性

**TL;DR 一句话：** 该文用 Laplace prior 建模角域 mmWave MIMO UAV-ground 信道稀疏性，并结合 EM/GAMP 稀疏特征提取与假设检验实现 UAV 链路 PHY-layer authentication。

**任务：** 输入对象是 mmWave MIMO UAV-ground 系统的角域信道观测；输出对象是链路认证判决以及虚警/检测概率分析；已知协议为基于信道稀疏相关、EM/GAMP 特征提取和 hypothesis testing 的物理层认证，主要通过数值结果验证。

**Argue 点：** 作者希望证明：角域 mmWave MIMO UAV-ground 信道可由 Laplace prior 高效建模，并且其稀疏空间相关性足以支撑高效的物理层认证框架，其虚警与检测性能可被理论闭式分析并由数值实验验证。

**核心创新：**

- 提出基于 Laplace prior 的 angular-domain mmWave MIMO channel 建模方法，用于刻画 UAV-ground 系统信道稀疏性。
- 将信道稀疏相关性、EM/GAMP 稀疏特征提取和 hypothesis testing 组合成 PHY-layer authentication 框架。
- 推导 false alarm 与 detection probabilities 的闭式表达式，用于理论性能分析。

**解决的问题／故事：** UAV-ground mmWave MIMO 链路需要认证，但该场景更依赖空间信道结构而非发射机硬件缺陷。现有认证若不能利用角域稀疏性，可能难以高效建模和判决。该文用 Laplace prior 和 EM/GAMP 提取稀疏信道特征，再用假设检验认证，摘要称数值结果验证模型、理论和多场景效率；但摘要未涉及真实硬件 RFFI 或跨接收机时间泛化。

---

#### 5. RaDro: Indoor Drone Tracking Using Millimeter Wave Radar

- ID：`2ef9680b11b67792`
- 作者：Heba Abdelnasser; Mohammad Heggo; Oscar Pang; M. Kovač; Julie A. McCann
- 发表：UbiComp，2024；出版社/正式索引记录
- Scope：雷达无人机跟踪/类型分类
- 核读依据：本地保存摘要；摘要级速读。
- 摘要来源：`https://openalex.org/W4402350770`
- DOI：[`10.1145/3678549`](https://doi.org/10.1145/3678549)
- 主要问题：空间定位跟踪与成像；次要问题：信号质量与可观测性、多目标干扰与分离

**TL;DR 一句话：** RaDro 用单个 mmWave 雷达点在室内无标签/无锚点跟踪无人机，实现 LoS/NLoS 下的 3D 定位、运动识别与检测，并较传统基线降低 50% 定位误差。

**任务：** 输入对象是室内 mmWave 雷达对无人机的反射/点迹信息；输出对象是无人机检测、运动识别和 3D localization/tracking 结果；已知协议包括不同无人机模型和尺寸、不同飞行动作、多个飞行场地、不同 clutter，以及 LoS/NLoS 和动态干扰场景。

**Argue 点：** 作者希望证明：无需 GPS、tags 或 anchors，仅依靠单个 mmWave 雷达点也能在复杂室内 LoS/NLoS 环境中稳健提取无人机运动与位置信息，并显著优于传统定位基线。

**核心创新：**

- 提出 RaDro 室内无人机 mmWave tracking 系统，以单个雷达点实现无标签、无锚点 3D tracking。
- 利用 mmWave 可穿透障碍物的特性覆盖 NLoS 场景，并面向检测、运动识别和定位同时提取粗粒度与细粒度信息。
- 在多无人机模型、多飞行动作、多场地、clutter、LoS/NLoS 和动态干扰条件下建立综合评测协议。

**解决的问题／故事：** 室内无人机无法稳定依赖 GPS，而光学方案在遮挡和 NLoS 下受限。RaDro 用 mmWave 雷达替代标签、锚点或视觉系统，面向复杂室内环境做检测、运动识别和定位。摘要报告相较传统基线定位误差降低 50%，且在其他移动源干扰和 NLoS 场景下仍可定位；但这属于雷达跟踪，不是通信设备硬件指纹识别。

---

### 2025（6 篇）

#### 1. A Multimodal Scale Normalization Framework for Vision-Radar Small UAV Positioning

- ID：`c60d2f1d463985b1`
- 作者：Yiyao Wan; Jiahuan Ji; Wenqing Xie; Guangyu Wu; Fu-Hui Zhou; Qi-Hui Wu
- 发表：TMC，2025；正式卷期/出版登记
- Scope：RF/雷达与视觉融合无人机检测/定位
- 核读依据：本地保存摘要；摘要级速读。
- 摘要来源：`https://openalex.org/W4408280709`
- DOI：[`10.1109/tmc.2025.3549620`](https://doi.org/10.1109/tmc.2025.3549620)
- 主要问题：跨模态对应与融合；次要问题：空间定位跟踪与成像、信号质量与可观测性

**TL;DR 一句话：** 该文提出 vision-radar 多模态尺度归一化框架，用 distance-aware slicing/scale normalization 与模态融合网络把远距离低分辨率 UAV patch 统一到一致尺度，从而提升像素级 UAV 定位鲁棒性。

**任务：** 输入对象是视觉图像中的低分辨率 UAV patches 及雷达距离等多模态信息；输出对象是一致实例尺度的高分辨率 UAV 图像和像素级 UAV positioning 结果；已知协议为可嵌入现有 pixel-level positioning pipelines，并在真实 vision-radar UAV positioning system 与真实世界数据集上验证。

**Argue 点：** 作者希望证明：把距离信息和视觉-雷达模态融合用于尺度归一化，可以缓解远距离小目标 UAV 的剧烈尺度变化，使现有像素级定位流程获得更好的定位性能与尺度鲁棒性。

**核心创新：**

- 提出 multimodal scale normalization framework，面向长距离小 UAV 的尺度鲁棒像素级定位。
- 设计 distance-aware image slicing 与 distance-aware scale normalization module，利用距离信息处理尺度变化。
- 提出 modal fusion-based scale normalization network，用单个可学习模型将任意低分辨率 UAV patches 生成统一实例尺度的高分辨率图像。

**解决的问题／故事：** 远距离 UAV 目标小且尺度随机动剧烈变化，导致像素级定位困难。单一视觉定位流程可能无法稳定处理尺度变化，因此该文引入雷达距离信息辅助视觉 patch 归一化。摘要称真实世界数据集证明框架通用有效，消融实验确认各模块贡献；但摘要未给出具体定位误差数值，也不涉及 RF 设备指纹认证。

---

#### 2. Challenge-Response to Authenticate Drone Communications: A Game Theoretic Approach

- ID：`5a81ca5be614c64c`
- 作者：Mattia Piana; F. Ardizzon; S. Tomasin
- 发表：TIFS，2025；正式卷期/出版登记
- Scope：UAV 链路信道认证；非硬件 RFFI
- 核读依据：本地保存摘要；摘要级速读。
- 摘要来源：`https://www.semanticscholar.org/paper/7af8251a65815c773e6fe38a38b85c5fb6a15a27`
- DOI：[`10.1109/tifs.2025.3566534`](https://doi.org/10.1109/tifs.2025.3566534)
- 主要问题：感知通信协同设计；次要问题：安全隐私与对抗、空间定位跟踪与成像

**TL;DR 一句话：** 该文把无人机移动位置作为 challenge、信道增益作为 response，并用零和博弈与多轮策略优化 CR-PLA，在安全性和能耗之间设计 UAV 通信认证协议。

**任务：** 输入对象是 verifier 指定的无人机移动位置 challenge、测得 channel gain response、入侵者位置策略及协议参数；输出对象是无人机消息真实性认证判决、多轮认证策略和能耗-安全性能；已知协议为 challenge-response PHY-layer authentication，数值仿真覆盖 urban/rural、不同高度和 drone swarms。

**Argue 点：** 作者希望证明：通过把位置移动 challenge 与信道增益 response 绑定，并用对抗入侵者的零和博弈生成混合策略，可以在多轮无人机通信认证中提高安全性，同时通过能量最小化控制合法无人机开销。

**核心创新：**

- 提出面向无人机消息的 challenge-response physical layer authentication（CR-PLA），以指定移动位置为 challenge、对应 channel gain 为 response。
- 将 challenge 选择建模为与入侵者位置策略对抗的 zero-sum game，并由 mixed strategy 生成认证挑战。
- 推导 multi-round authentication 最优策略，并加入不损害安全性能的 energy minimization 设计。

**解决的问题／故事：** 无人机通信需要认证，但入侵者可伪造消息，单次静态信道检查可能不足。该文让 verifier 主动要求无人机移动，并用位置相关信道增益验证真实性，同时用博弈策略考虑入侵者位置选择。摘要称仿真从安全和能耗两方面测试，覆盖城乡、高度和蜂群场景；但认证依据是信道/位置响应，不是硬件 RF 指纹。

---

#### 3. DroneMA: Drone Mobility Alignment Countering AI-Based Spoofing Attacks

- ID：`77488b1b39bf42df`
- 作者：Weiyang Li; Ning Wang; Chuan Ma; Tao Xiang; Kai Zeng
- 发表：INFOCOM，2025；出版社/正式索引记录
- Scope：UAV 链路信道认证；非硬件 RFFI
- 核读依据：本地保存摘要；摘要级速读。
- 摘要来源：`https://mr3white.github.io/assets/DroneMA.pdf`
- DOI：[`10.1109/infocom55648.2025.11044631`](https://doi.org/10.1109/infocom55648.2025.11044631)
- 主要问题：安全隐私与对抗；次要问题：效率与边缘部署、未知目标与可靠拒识

**TL;DR 一句话：** DroneMA 用 RSSI 时间变化刻画无人机相对 GCS 与攻击者的 mobility characteristics，经 Z-score+GRU 特征对齐和 IQR 单正样本检测实现资源受限 UAV spoofing detection。

**任务：** 输入对象是无人机接收信号强度 RSSI 的变化趋势及其时序特征；输出对象是合法信号/欺骗信号检测结果；已知协议为 off-the-shelf devices 可实现，使用 Z-score normalization、GRU feature alignment 和 IQR-based detection，仅依赖 positive samples 建模，并在三种典型飞行场景真实实验评估。

**Argue 点：** 作者希望证明：由于无人机相对攻击者和合法 GCS 的位置/运动关系天然不同，RSSI 变化趋势中的 mobility characteristics 可用于区分 spoofing 与 legitimate signals，并且通过特征对齐和 IQR 单正样本检测能适应 RSSI 不准与未知攻击模型。

**核心创新：**

- 提出 DroneMA mobility alignment-based spoofing detection framework，以无人机相对 GCS 与攻击者的运动差异作为物理层判别依据。
- 用 RSSI variation trend 捕捉 mobility characteristics，并通过 Z-score normalization 与 GRU network 进行 feature alignment 以缓解 RSSI 不准确。
- 设计基于 Interquartile Range（IQR）的检测方案，使模型仅用 positive samples 即可面对不可预测攻击模型。

**解决的问题／故事：** 生成式 AI 可能让物理层欺骗信号更像合法传输，而无人机资源有限，难以部署复杂检测。DroneMA 不直接依赖信号内容相似度，而利用合法 GCS 与攻击者相对运动关系不同导致的 RSSI 趋势差异。摘要报告真实世界三种典型飞行场景平均准确率 92.78%；但它检测的是 spoofing 信号的运动一致性，不是发射机硬件个体 RFFI。

---

#### 4. Enhanced Two-Way Privacy-Preserving PHY-Layer Authentication for UAV-Assisted MIMO Systems

- ID：`cc499c31736884a6`
- 作者：Pin-Chang Zhang; Huangwenqing Shi; Jian-Kuo Dong; Ji He; Xiao-Hong Jiang; Fu Xiao
- 发表：TDSC，2025；正式卷期/出版登记
- Scope：UAV RF 硬件特征认证（CFO）
- 核读依据：本地保存摘要；摘要级速读。
- 摘要来源：`https://www.semanticscholar.org/paper/a5995af9fadf0db713ca3b63fd27bf0d84d28a61`
- DOI：[`10.1109/tdsc.2025.3594095`](https://doi.org/10.1109/tdsc.2025.3594095)
- 主要问题：安全隐私与对抗；次要问题：设备身份与物理归属、硬件测量与成像系统

**TL;DR 一句话：** 该文用MOOSE提取UAV CFO硬件指纹，并用ECC基于CFO协商会话密钥，在UAV辅助MIMO系统中同时完成双向PHY-Layer认证与数据帧隐私保护。

**任务：** 输入为UAV辅助MIMO通信中的接收信号/帧及其可估计CFO参数，输出为网络双方身份认证结果、会话密钥和加密数据帧；协议包含MOOSE CFO提取、ECC会话密钥协商、基于CFO参数的双向认证，并给出检测概率与虚警概率解析评估。

**Argue 点：** 作者希望证明：UAV的CFO可作为稳定身份相关硬件指纹，并能与ECC会话密钥机制结合，在UAV辅助MIMO系统中相较既有方案同时提升身份认证鲁棒性与隐私保护能力。

**核心创新：**

- 将MOOSE algorithm提取的CFO硬件指纹用于UAV身份表征，为PHY-Layer认证提供可测量的设备相关特征。
- 设计基于CFO特征参数的ECC会话密钥协商，并用该密钥加密数据帧，使认证特征同时服务于隐私保护。
- 建立基于CFO参数的双向认证框架，并推导检测概率和虚警概率的闭式表达式以支持理论性能分析。

**解决的问题／故事：** UAV辅助通信需要确认通信实体身份，同时不能因认证过程泄露私人数据。既有认证方案往往偏重身份验证，对数据帧隐私和双向认证的联合处理不足。该文把CFO硬件指纹、ECC密钥协商和双向PHY-Layer认证绑定起来，摘要中的数值结果声称验证了理论模型，并显示身份认证与隐私保护有效。需要注意，摘要只说明数值结果和与先前方案比较，未给出真实采集数据、跨接收机或长期部署条件。

---

#### 5. From Static Dense to Dynamic Sparse: Vision-Radar Fusion-Based UAV Detection

- ID：`ebb11fba47b75592`
- 作者：Yiyao Wan; Jiahuan Ji; Fu-Hui Zhou; Qi-Hui Wu; Tony Q. S. Quek
- 发表：TIFS，2025；正式卷期/出版登记
- Scope：RF/雷达与视觉融合无人机检测/定位
- 核读依据：本地保存摘要；摘要级速读。
- 摘要来源：`https://openalex.org/W4409427393`
- DOI：[`10.1109/tifs.2025.3560551`](https://doi.org/10.1109/tifs.2025.3560551)
- 主要问题：跨模态对应与融合；次要问题：空间定位跟踪与成像、信号质量与可观测性

**TL;DR 一句话：** 该文用雷达引导的动态稀疏候选生成和语义特征变换融合视觉与雷达数据，实现远距离小型高机动UAV实时检测。

**任务：** 输入为视觉图像和雷达数据，输出为UAV检测结果；已知协议包括雷达驱动的动态稀疏候选生成、雷达引导语义特征变换、Hungarian bisection matching端到端匹配，并在实际视觉-雷达融合检测系统中测试。

**Argue 点：** 作者希望证明：相较静态稠密视觉检测范式，利用雷达数据动态生成稀疏候选和语义特征能更好处理UAV小尺寸、高机动导致的候选不平衡问题，从而提升实时远距离检测精度与召回。

**核心创新：**

- 提出多模态融合的动态稀疏UAV检测框架，用雷达数据动态重构检测先验。
- 设计Vira-DSNet中的dynamic sparse candidate generator和radar-guided semantic feature transform，生成少量高质量候选和语义特征。
- 采用Hungarian bisection matching使检测流程去除后处理并保持端到端可微。

**解决的问题／故事：** 空域安全需要在远距离发现小型高速移动UAV。单纯视觉深度检测依赖固定先验，面对小目标和高机动目标时存在密集候选失衡与错配。该文用雷达信息指导视觉检测候选与语义特征，摘要报告AP50为88.2%、AR1较SOTA高10.1%且保持实时。边界是该任务是UAV检测而非设备硬件个体识别，摘要未涉及RFFI跨源域泛化。

---

#### 6. UAV-Assisted Communications in SAGIN-ISAC: Mobile User Tracking and Robust Beamforming

- ID：`48ccd3e8bddd35be`
- 作者：Wei-Hao Mao; Yang Lu; Gao-Feng Pan; Bo Ai
- 发表：JSAC，2025；正式卷期/出版登记
- Scope：UAV 平台 + ISAC 用户跟踪/能效外围
- 核读依据：本地保存摘要；摘要级速读。
- 摘要来源：`https://openalex.org/W4402509610`
- DOI：[`10.1109/jsac.2024.3460065`](https://doi.org/10.1109/jsac.2024.3460065)
- 主要问题：感知通信协同设计；次要问题：空间定位跟踪与成像、效率与边缘部署

**TL;DR 一句话：** 该文在SAGIN-ISAC中用卫星辅助或EKF式ISAC辅助位置获取来预测MU信道，并联合鲁棒波束成形优化UAV能效。

**任务：** 输入为UAV在SAGIN-ISAC系统中获取的MU位置信息或回波估计信息、信道分布和通信约束，输出为MU跟踪轨迹、UAV波束成形方案和能效表现；协议包含space-assisted定位、ISAC-assisted extended Kalman filter定位、Bernstein-type inequality约束重构、SDR与successive convex approximation求解。

**Argue 点：** 作者希望证明：在SAGIN中集成ISAC并利用UAV获得/估计MU位置，可在减少空间段信息需求的同时支持鲁棒波束成形和带中断约束的能效优化。

**核心创新：**

- 提出space-assisted与ISAC-assisted两种UAV获取MU位置信息的方案，分别依赖卫星传输和extended Kalman filter估计。
- 将位置信息用于预测MU信道分布，并构造带中断约束的EE最大化问题。
- 用Bernstein-type inequality、SDR和successive convex approximation处理概率约束优化，并证明SDR紧性。

**解决的问题／故事：** 未来SAGIN-ISAC需要UAV同时服务通信与感知，但移动用户位置不确定会影响信道预测和能效优化。传统SAGIN若强依赖卫星精确位置，会带来space-air transmission开销。该文比较卫星辅助和ISAC辅助定位，再把位置预测用于鲁棒波束成形，摘要证据显示存在传输开销与位置精度的权衡，并且ISAC可减少空间信息需求。该工作不是UAV硬件身份识别，也未涉及RF指纹泛化。

---

### 2026（8 篇）

#### 1. "Take Me Home, Wi-Fi Drone": A Drone-based Wireless System for Wilderness Search and Rescue

- ID：`871947253a81c530`
- 作者：Weiying Hou; Luca Jiang-Tao Yu; Chenshu Wu
- 发表：MobiCom，2026；已接收主会长文；正式出版日期另核
- Scope：UAV 平台 + WiFi 搜救定位
- 核读依据：本地保存摘要；摘要级速读。
- 摘要来源：`https://openalex.org/W7154290013`
- DOI：[`未核得正式 DOI`](https://doi.org/未核得正式 DOI)
- 主要问题：空间定位跟踪与成像；次要问题：信号质量与可观测性、效率与边缘部署

**TL;DR 一句话：** 该文让无人机伪装已知Wi-Fi网络触发手机自动重连，并用RSS-only Luneburg Lens测向与自适应导航实现野外搜救定位。

**任务：** 输入为受害者移动设备对机载Wi-Fi模仿网络的响应/RSS观测，输出为设备发现、目标受害者识别、方向估计和无人机导航路径；协议包括机载Wi-Fi网络模仿、快速节能设备发现、3D打印Luneburg Lens的RSS-only长距离测向、自适应无人机导航，以及多设备真实野外原型评估。

**Argue 点：** 作者希望证明：利用移动设备自动重连行为并结合机载Wi-Fi、RSS-only方向增强测量和自适应导航，可以在无基础设施、长距离、穿遮挡的野外搜救中有效发现并定位受害者。

**核心创新：**

- 利用现代Wi-Fi设备对已知网络的自动重连行为，由无人机模仿网络以发现和定位受害者随身设备。
- 提出快速节能的设备发现机制，用于发现并识别目标受害者。
- 提出基于3D打印Luneburg Lens的RSS-only长距离测向方法，并配合自适应无人机导航逼近目标。

**解决的问题／故事：** 野外搜救需要在无基础设施、遮挡环境和大范围区域内快速找到失联人员。传统方案难以依赖现有网络，也难以让无人机高效获得受害者方向信息。Wi2SAR把手机自动重连行为转化为可触发的无线发现信号，再用Luneburg Lens增强RSS方向差异并导航接近目标，摘要称在多种移动设备和真实野外场景中表现出高性能与实用性。边界是该文识别的是受害者/设备目标用于定位，不是基于硬件指纹的个体发射机RFFI。

---

#### 2. AirGuard: UAV and Bird Recognition Scheme for Integrated Sensing and Communications System

- ID：`83c6721aebe95752`
- 作者：Hongliang Luo; Zhonghua Chu; Teng-Yu Zhang; Chuanbin Zhao; Bo Lin; Feifei Gao
- 发表：JSAC，2026；正式卷期/出版登记
- Scope：UAV × RF 感知/识别
- 核读依据：本地保存摘要；摘要级速读。
- 摘要来源：`https://openalex.org/W4414155255`
- DOI：[`10.1109/jsac.2025.3608760`](https://doi.org/10.1109/jsac.2025.3608760)
- 主要问题：信号质量与可观测性；次要问题：空间定位跟踪与成像、数据集与评测协议

**TL;DR 一句话：** AirGuard从ISAC回波中提取cmD spectrum和HRRP图像，并用CNN双特征融合区分低空UAV与鸟类。

**任务：** 输入为ISAC系统中低空目标回波信号，输出为UAV或鸟类类别；协议包括建立UAV/鸟类运动方程与回波模型、提取cmD spectrum和HRRP、生成237600个图像样本、用CNN双特征融合网络训练验证评估。

**Argue 点：** 作者希望证明：cmD spectrum和HRRP分别携带低空目标运动微多普勒与距离轮廓信息，将二者图像联合输入CNN可有效区分UAV和鸟类。

**核心创新：**

- 在ISAC低空监测场景中同时建模UAV与鸟类运动方程和回波信号。
- 从回波信号中联合提取cmD spectrum与HRRP，形成双特征输入。
- 设计CNN双特征融合低空目标识别网络，并用237600个生成样本进行训练、验证和评估。

**解决的问题／故事：** 低空安全监测需要区分无人机与鸟类，避免把自然目标和潜在威胁混淆。单一回波特征可能难以同时刻画目标运动和距离结构。AirGuard把cmD与HRRP两种RF感知视图融合进CNN，摘要称仿真结果证明有效。边界是多个频率/谱图视图仍属于同一RF感知模态，不等同于跨模态融合，也不是发射机硬件个体RFFI。

---

#### 3. Lightweight Memory Network for Drone Type RF Fingerprint Identification in Dynamic Environments

- ID：`595d5a5d507a745e`
- 作者：Fei-Fei Zhu; Fu-Hui Zhou; Qi-Hui Wu
- 发表：TIFS，2026；正式卷期/出版登记
- Scope：UAV RF 类型识别；个体协议待核
- 核读依据：本地保存摘要；摘要级速读。
- 摘要来源：`https://ieeexplore.ieee.org/abstract/document/11695277/`
- DOI：[`10.1109/tifs.2026.3734750`](https://doi.org/10.1109/tifs.2026.3734750)
- 主要问题：时间漂移与持续部署；次要问题：设备身份与物理归属、信号质量与可观测性

**TL;DR 一句话：** 该文用多尺度spectrogram、通道/空间注意力、全局-局部双路径和可训练memory/gate做动态环境下无人机RF类别识别。

**任务：** 输入为动态遮挡传播环境中的无人机RF指纹spectrogram，输出为九类无人机类别识别结果；已知协议为新采集九类别数据集评估，并包含组件消融，但摘要中的个体识别协议与同类内不同发射机验证尚未核实。

**Argue 点：** 作者希望证明：在传播遮挡和时间变化下，紧凑的多尺度spectrogram特征提取、注意力、全局/局部关系建模以及memory-gate融合能提升无人机RF识别准确率。

**核心创新：**

- 将多尺度spectrogram特征与channel and spatial attention结合，以增强动态环境下RF表征。
- 用全局和局部两条互补路径建模不同范围的特征关系。
- 引入可训练memory存储跨样本共享信息，并用gate自适应融合表示。

**解决的问题／故事：** 动态传播、遮挡和时间变化会削弱无人机RF指纹识别的稳定性。单一尺度或单一路径网络可能难以同时捕获局部谱纹和全局关系。该文提出轻量memory网络，摘要报告九类别数据集平均识别准确率95.16%，并称消融支持各组件贡献。边界很重要：摘要筛查文本显示评估更偏无人机类别识别，是否为同型号内硬件个体RFFI仍需核全文协议。

---

#### 4. MAPRT Detector-Based Air-Ground ISAC Systems: Joint UAV Placement and Precoding

- ID：`7e02d25553c6cb43`
- 作者：Linlin Xu; Wenchao Xia; Yong-Xu Zhu; Qi Zhu; Wei Feng
- 发表：JSAC，2026；正式卷期/出版登记
- Scope：UAV 平台 + ISAC 雷达目标检测
- 核读依据：本地保存摘要；摘要级速读。
- 摘要来源：`https://openalex.org/W4414229927`
- DOI：[`10.1109/jsac.2025.3610423`](https://doi.org/10.1109/jsac.2025.3610423)
- 主要问题：感知通信协同设计；次要问题：空间定位跟踪与成像、信号质量与可观测性

**TL;DR 一句话：** 该文在空地ISAC中让UAV主动发射、地面AP被动接收反射信号，并用MAPRT与联合UAV位置/波束优化提升目标检测。

**任务：** 输入为UAV主动ISAC信号的目标回波、地面AP接收的反射信号、反射系数分布知识和通信QoS约束，输出为潜在目标检测/融合决策以及UAV位置和发射波束成形方案；协议包括本地检测、结果融合、MAPRT detector、渐近分布推导和联合优化。

**Argue 点：** 作者希望证明：把地面AP作为被动感知接收机并结合MAPRT检测与UAV位置/波束联合优化，可在回传受限条件下提升UAV赋能空地ISAC的目标检测性能。

**核心创新：**

- 提出UAV主动发射与地面AP被动接收协同的空地ISAC检测架构。
- 设计包含本地检测和结果融合的两步联合检测方法，以适应无线回传容量限制。
- 提出利用反射系数分布知识的MAPRT detector，并联合优化UAV placement和transmit beamformer以最小化融合错误概率。

**解决的问题／故事：** UAV-ISAC系统若只依赖UAV自身感知，会浪费地面AP可接收反射信号的潜力。回传链路容量有限又要求本地检测和融合不能传输过多原始信息。该文提出空地协作检测、MAPRT和联合位置/波束优化，摘要中的数值结果声称算法有效。该工作关注目标检测和ISAC资源设计，不涉及发射机硬件指纹身份。

---

#### 5. MIROS: Elusive Unauthorized AAV Positioning by Multi-View Radar-Vision Cognitive Fusion

- ID：`d7b09722c8bca1e1`
- 作者：Guangyu Wu; Yuxin Zhao; Hai-Bo Zhou; Yu-Ben Qu; Kai-Kuang Ma
- 发表：INFOCOM，2026；出版社/正式索引记录
- Scope：RF/雷达与视觉融合无人机检测/定位
- 核读依据：本地保存摘要；摘要级速读。
- 摘要来源：`https://www.semanticscholar.org/paper/6016e38ea1fb7bb82bab72130625b9b3686546de`
- DOI：[`10.1109/infocom59046.2026.11571625`](https://doi.org/10.1109/infocom59046.2026.11571625)
- 主要问题：跨模态对应与融合；次要问题：空间定位跟踪与成像、多目标干扰与分离

**TL;DR 一句话：** MIROS用OODA认知循环组织多视角雷达-视觉融合，通过abstract-binding和情境感知协同感知实现隐蔽AAV大范围实时定位。

**任务：** 输入为一部雷达和三台视觉监视器等多视角异构传感器数据，输出为未经授权AAV的位置与识别结果；协议包括OODA循环、abstract-binding跨模态/跨视角融合、基于动力学建模的situation-aware多视角协同感知，以及月级真实部署评估。

**Argue 点：** 作者希望证明：分布式多视角雷达-视觉认知融合比单模态或单视角方案更能抵抗环境不利和观测受限，从而实现隐蔽AAV的高精度、实时、可扩展定位与识别。

**核心创新：**

- 以OODA认知循环组织分布式多视角Radar-vision融合定位框架。
- 提出abstract-binding-based fusion strategy，通过学习跨模态和跨视角相关性自适应融合异构数据。
- 提出situation-aware multi-view collaborative sensing strategy，利用动力学建模主动协调多视角传感器。

**解决的问题／故事：** 公共安全场景需要在大范围内定位小型、轨迹不可预测的未经授权AAV。单模态或单视角方案在环境恶劣和观测有限时容易出现定位和识别退化。MIROS用雷达-视觉多视角认知融合闭合观察、定向、决策和行动循环，摘要报告月级部署中9.6 cm定位误差和最高2.14×识别准确率提升。边界是其“识别”面向目标检测/定位语境，不是硬件个体RFFI。

---

#### 6. mmE-Loc: Facilitating Accurate Drone Landing With Ultra-High-Frequency Localization

- ID：`159547b27ad94845`
- 作者：Hao-Yang Wang; Jin-Gao Xu; Xinyu Luo; Ting Zhang; Xue-Cheng Chen; Ruiyang Duan; Yun-Hao Liu; Jianfeng Zheng; Wei-Jie Hong; Xiao-Qiang Ji; Yu-Qing Tang; Xinlei Chen
- 发表：TMC，2026；正式卷期/出版登记
- Scope：RF/雷达与视觉融合无人机检测/定位
- 核读依据：本地保存摘要；摘要级速读。
- 摘要来源：`https://openalex.org/W7130562114`
- DOI：[`10.1109/tmc.2026.3666235`](https://doi.org/10.1109/tmc.2026.3666235)
- 主要问题：跨模态对应与融合；次要问题：空间定位跟踪与成像、效率与边缘部署

**TL;DR 一句话：** mmE-Loc融合event camera与mmWave radar，用一致性协同跟踪和图引导自适应联合优化实现无人机降落的低时延高精度定位。

**任务：** 输入为地面平台上的event camera事件流和mmWave radar观测，输出为下降无人机的实时定位结果和降落引导依据；协议包括替换frame camera为event camera、Consistency-instructed Collaborative Tracking、Graph-informed Adaptive Joint Optimization，以及30+小时实验评估。

**Argue 点：** 作者希望证明：event camera与mmWave radar在采样频率上更协调，结合时间一致性、空间互补性和无人机运动物理知识，可比传统相机-mmWave方案实现更高吞吐、更低时延和更精确的无人机降落定位。

**核心创新：**

- 用event camera替代传统frame camera，使视觉传感采样频率更匹配mmWave radar，缓解系统吞吐瓶颈。
- 提出Consistency-instructed Collaborative Tracking，利用无人机周期性微运动和结构物理知识提取准确测量。
- 提出Graph-informed Adaptive Joint Optimization，整合无人机运动信息以进行高效传感器融合和定位。

**解决的问题／故事：** 精准无人机降落要求地面平台实时定位下降目标，延迟和精度都很关键。传统相机与mmWave radar融合虽然有效，但frame camera采样频率低限制吞吐。mmE-Loc使用event camera和mmWave radar，并通过两个融合优化模块利用时间一致性和空间互补性，摘要报告0.083 m精度和5.12 ms端到端时延。该工作是定位系统，不是RF硬件指纹认证。

---

#### 7. Multi-Domain Supervised Contrastive Learning for UAV Radio-Frequency Open-Set Recognition

- ID：`c0da9c9145f3b86b`
- 作者：Ning Gao; Tianrui Zeng; Bo-Wen Chen; Donghong Cai; Shi Jin; M. Matthaiou
- 发表：JSAC，2026；正式卷期/出版登记
- Scope：RF 无人机开放集识别
- 核读依据：本地保存摘要；摘要级速读。
- 摘要来源：`https://openalex.org/W7133235294`
- DOI：[`10.1109/jsac.2026.3669136`](https://doi.org/10.1109/jsac.2026.3669136)
- 主要问题：未知目标与可靠拒识；次要问题：少标签与自监督、数据集与评测协议

**TL;DR 一句话：** Open-RFNet用ResNet/TE多域RF特征融合、supervised contrastive learning和IG-OpenMax实现25种UAV类型的RF开集识别。

**任务：** 输入为UAV RF样本的纹理特征和时频位置特征，输出为已知UAV类型分类和未知UAV拒识/开集识别结果；协议包括ResNet与TransformerEncoder特征融合、MD-SupContrast闭集表征优化、IG-OpenMax开集建模、冻结特征提取层后仅重训分类层，并在大规模UAV开放数据集25种类型上评估。

**Argue 点：** 作者希望证明：融合RF纹理与时频位置特征，并用监督对比学习优化闭集表征，再结合改进OpenMax，可同时提升已知UAV类型识别和未知入侵UAV开集识别性能。

**核心创新：**

- 提出MD-SupContrast框架，将ResNet纹理特征与TransformerEncoder时频位置特征融合，并用supervised contrastive learning优化闭集表征。
- 提出IG-OpenMax算法并构建Open-RFNet，用于现实未知入侵UAV的RF开集识别。
- 采用冻结特征提取层、仅重训分类层的未知样本适配流程，并分析模型计算复杂度。

**解决的问题／故事：** LA-ISAC中的非合作UAV监管需要识别已知类型，也要发现未见过的入侵目标。传统闭集分类容易把未知UAV强行归入已知类别，安全风险较高。Open-RFNet把多域RF特征、监督对比学习和IG-OpenMax结合，摘要报告在25种UAV类型下闭集95.12%、开集96.08%。边界是摘要强调UAV类型级开集识别，不能自动等同于同型号内硬件个体RFFI；其中“根据未知样本”再训练分类层也不是严格source-only设置。

---

#### 8. Precise RF-Vision Fusion UAV Positioning and Identification for 6G Spectrum Security

- ID：`004c49e14d0c63c0`
- 作者：Yiyao Wan; Hong-Tao Liang; Guangyu Wu; Fu-Hui Zhou; Bruno Crispo; Qi-Hui Wu
- 发表：JSAC，2026；正式卷期/出版登记
- Scope：RF/雷达与视觉融合无人机检测/定位
- 核读依据：本地保存摘要；摘要级速读。
- 摘要来源：`https://openalex.org/W7133774256`
- DOI：[`10.1109/jsac.2026.3671229`](https://doi.org/10.1109/jsac.2026.3671229)
- 主要问题：跨模态对应与融合；次要问题：空间定位跟踪与成像、信号质量与可观测性、数据集与评测协议

**TL;DR 一句话：** RFViNet 用 RF 时频特征引导视觉 proposal、特征调制和语义查询，实现非法 UAV 的 RF-vision 融合定位与识别，并在真实平台上达到 85.8% AP50。

**任务：** 输入为 UAV RF 信号的 temporal-spectral 特征与视觉图像/空间视觉信息，输出为 UAV 的位置与身份/类别识别结果；已知协议为作者自建 practical RF-vision platform，在多种挑战条件和真实世界数据集上评估 AP50。

**Argue 点：** 作者希望证明：相比受单一传感器噪声限制的单模态方案，利用 RF-informed proposal generation、RF-enhanced feature modulation 和 RF-guided semantic query 的多层 RF-vision 融合，可以更精确且鲁棒地完成未经授权 UAV 的定位与识别。

**核心创新：**

- 提出多层 RF-vision fusion 框架，将 UAV RF 信号的时频特征与视觉空间信息协同用于定位和识别。
- 设计 RFViNet，通过 RF-informed proposal generation、RF-enhanced feature modulation、RF-guided semantic query 三类模块把 RF 线索注入视觉检测/语义推理流程。
- 搭建 practical RF-vision platform，在真实世界挑战条件下评估 RF-视觉融合方法。

**解决的问题／故事：** 未来智能网络需要及时发现并定位未经授权 UAV，以保护频谱安全和隐私。现有单模态方案容易受传感器特有噪声影响，定位和识别鲁棒性不足。RFViNet 用 RF 时频信息约束和增强视觉检测流程，摘要证据给出真实世界数据集 85.8% AP50；但摘要未说明数据规模、跨地点/跨设备泛化、开集拒识或消融细节，需核全文。

---
