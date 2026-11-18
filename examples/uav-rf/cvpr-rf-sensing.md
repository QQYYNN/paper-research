[English README](../../README.md) · [中文 README](../../README.zh-CN.md) · [Walkthrough (EN)](README.md) · [全流程样例 (中文)](README.zh-CN.md)

# CVPR 2024 · RF 感知 / RF sensing

节选自历史调研文档 `paper-story-cards.md`。保留选中段落的原有卡片文字、编号和顺序。出版社摘要、摘要译文和本地文件路径经删节，论文链接可用于查阅原摘要。

Excerpt from the original `paper-story-cards.md` in the survey archive. Card notes, numbering, and order are preserved in Chinese. Publisher abstracts, their translations, and local paths are omitted. Follow the paper links for the abstracts.

## 原始卡片 / Original cards

### 38. CRKD: Enhanced Camera-Radar Object Detection with Cross-modality Knowledge Distillation

- **Scope：** `radar-perception`
- **TL;DR 一句话：** CRKD 以 BEV 为共享特征空间，将 LiDAR-Camera 教师的知识蒸馏给 Camera-Radar 学生，从而提升低成本传感器配置的三维目标检测能力。
- **任务：** 任务是在 nuScenes 上输入相机与雷达数据进行三维目标检测，并利用训练期的 LiDAR-Camera 检测器缩小 Camera-Radar 与 LiDAR-Camera 融合的性能差距。
- **Argue 点：** 作者主张，借助适配跨模态路径的 BEV 知识蒸馏，Camera-Radar 检测器能够有效吸收高性能 LiDAR-Camera 检测器的关键表征。
- **核心创新：**
  - 提出 Camera-Radar Knowledge Distillation（CRKD）跨模态知识蒸馏框架。
  - 以鸟瞰视图（BEV）作为教师与学生之间的共享特征空间。
  - 设计四种蒸馏损失，帮助学生模型学习教师模型的关键特征。
- **解决的问题 / 故事：** LiDAR-Camera 融合性能领先，但 LiDAR 成本限制了其在消费级汽车中的普及，而更常见的 Camera-Radar 融合仍存在性能差距。CRKD 在 BEV 共享空间中建立从 LiDAR-Camera 教师到 Camera-Radar 学生的跨模态知识迁移，并以四种损失约束蒸馏过程。摘要称，nuScenes 上的广泛评估证明了该框架的有效性，但未给出具体提升数值。

[CVF Open Access](https://openaccess.thecvf.com/content/CVPR2024/html/Zhao_CRKD_Enhanced_Camera-Radar_Object_Detection_with_Cross-modality_Knowledge_Distillation_CVPR_2024_paper.html)

---

### 39. DART: Implicit Doppler Tomography for Radar Novel View Synthesis

- **Scope：** `rf-wireless-sensing`
- **TL;DR 一句话：** DART 将雷达物理融入受 Neural Radiance Field 启发的隐式表示，可从新视角合成高质量距离-多普勒图像并生成层析图像。
- **任务：** 任务是根据带有准确位姿和瞬时速度测量的雷达观测，渲染未观测视角的距离-多普勒图像，并支持雷达层析成像。
- **Argue 点：** 作者主张，无需显式构建场景几何、射频材料属性和雷达合成函数，结合多普勒信息与雷达物理的隐式模型也能逼真地重建和渲染雷达场景。
- **核心创新：**
  - 提出 Doppler Aided Radar Tomography（DART），将雷达特有物理规律引入受 Neural Radiance Field 启发的隐式建模。
  - 构建基于反射率与透射率的距离-多普勒图像渲染流程。
  - 搭建定制采集平台并发布包含雷达数据、LiDAR 定位位姿及瞬时速度测量的新数据集。
- **解决的问题 / 故事：** 逼真雷达仿真通常依赖准确的场景、材料属性与合成函数，因而建模困难。DART 用隐式反射率和透射率表示结合多普勒信息，绕过这些显式模型并实现新视角渲染。摘要报告其在所有数据集上优于当前最先进基线生成距离-多普勒图像，同时还能产生高质量层析图像，但未给出具体指标。

[CVF Open Access](https://openaccess.thecvf.com/content/CVPR2024/html/Huang_DART_Implicit_Doppler_Tomography_for_Radar_Novel_View_Synthesis_CVPR_2024_paper.html)

---

### 40. MSU-4S - The Michigan State University Four Seasons Dataset

- **Scope：** `radar-perception`
- **TL;DR 一句话：** MSU-4S 提供跨四季、天气和时段配准采集的多传感器自动驾驶数据，以支持域偏移分析及 Camera-LiDAR-Radar 融合研究。
- **任务：** 任务是利用超过 100000 帧相机、LiDAR、雷达、GNSS、轮速和转向数据，评估不同季节与天气下的二维、三维目标检测及多模态融合。
- **Argue 点：** 作者主张，几乎对同一场景进行四季重复采集并提供丰富条件标注，是系统研究天气域偏移和自动驾驶感知鲁棒性的关键数据基础。
- **核心创新：**
  - 发布 Michigan State University Four Seasons（MSU-4S）Dataset，覆盖晴天、雨天、雪天和秋季场景以及不同时段。
  - 提供超过 100000 帧二维和三维相机、LiDAR、雷达数据，并同步包含 GNSS、轮速与转向信息。
  - 几乎每个场景及其多传感器帧均跨四季采集，并标注天气、时段和季节。
- **解决的问题 / 故事：** KITTI、nuScenes 和 Waymo 等数据集未充分覆盖雪天、秋季等多样驾驶条件，限制了跨天气鲁棒性研究。MSU-4S 通过跨四季重复采集真实道路场景，汇集多传感器与车辆状态数据，为目标检测和模态融合提供可比较样本。二维与三维目标检测分析显示，不同采集条件的数据片段之间存在显著域偏移效应。

[CVF Open Access](https://openaccess.thecvf.com/content/CVPR2024/html/Kent_MSU-4S_-_The_Michigan_State_University_Four_Seasons_Dataset_CVPR_2024_paper.html)

---

### 41. Person-in-WiFi 3D: End-to-End Multi-Person 3D Pose Estimation with Wi-Fi

- **Scope：** `rf-wireless-sensing`
- **TL;DR 一句话：** Person-in-WiFi 3D 利用更多 Wi-Fi 设备和 Transformer 端到端估计多人三维姿态，在保护隐私并抵抗遮挡的同时取得可比于相机和毫米波雷达的定位精度。
- **任务：** 任务是在 4m×3.5m 区域内，根据 Wi-Fi 信号端到端输出 1 至 3 人的三维关节位置，并评估不同人数下的定位误差、速度和存储效率。
- **Argue 点：** 作者主张，通过增强多人体空间反射采集能力并采用 Transformer 端到端建模，Wi-Fi 能够胜任此前尚未解决的多人三维姿态估计。
- **核心创新：**
  - 提出可执行多人三维姿态估计的 Person-in-WiFi 3D 系统。
  - 增加 Wi-Fi 设备数量以捕获多个人体的空间反射，并利用 Transformer 进行端到端估计。
  - 构建由七名志愿者参与、包含超过 97K 帧的数据集。
- **解决的问题 / 故事：** Wi-Fi 具备隐私保护和抗遮挡优势，但既有研究主要覆盖单人二维、单人三维或多人二维姿态估计。Person-in-WiFi 3D 通过增加设备数量和引入 Transformer，将能力推进到多人三维关节定位，并较前代系统提高速度与存储效率。其三维关节定位误差为 91.7mm（1 人）、108.1mm（2 人）和 125.3mm（3 人），摘要称这一水平可与相机和毫米波雷达媲美。

[CVF Open Access](https://openaccess.thecvf.com/content/CVPR2024/html/Yan_Person-in-WiFi_3D_End-to-End_Multi-Person_3D_Pose_Estimation_with_Wi-Fi_CVPR_2024_paper.html)

---

### 42. PolarRec: Improving Radio Interferometric Data Reconstruction Using Polar Coordinates

- **Scope：** `radar-perception`
- **TL;DR 一句话：** PolarRec 在与射电望远镜观测规律匹配的极坐标系中重建可见度数据，从而改善射电成像质量并降低不规则样本编码开销。
- **任务：** 任务是将稀疏、不规则的射电干涉可见度样本重建为稠密频域数据，再输出伪影更少、边缘更清晰的天体图像。
- **Argue 点：** 作者主张，相比笛卡尔空间，极坐标表示能让可见度样本分布更均匀，并使模型更完整且高效地恢复各频率分量。
- **核心创新：**
  - 提出 Transformer 编码器条件化的 PolarRec 重建流程，将可见度样本转换到极坐标系。
  - 在损失函数中引入径向距离，以促进完整可见度重建。
  - 按极角划分样本并设计基于分组的编码方案，以降低计算成本。
- **解决的问题 / 故事：** 稀疏射电干涉数据会使成像结果同时包含真实源与伪影，而既有重建方法还会遗漏频率分量并受不规则数据偏斜带来的高开销影响。PolarRec 利用符合地球自转观测轨迹的极坐标表示，结合径向距离损失和极角分组编码解决完整性与效率问题。摘要报告该方法能忠实重建全部频率分量、显著改善成像结果并大幅降低编码计算成本，但未给出具体数值。

[CVF Open Access](https://openaccess.thecvf.com/content/CVPR2024/html/Wang_PolarRec_Improving_Radio_Interferometric_Data_Reconstruction_Using_Polar_Coordinates_CVPR_2024_paper.html)

---

### 43. RadarDistill: Boosting Radar-based Object Detection Performance via Knowledge Distillation from LiDAR Features

- **Scope：** `radar-perception`
- **TL;DR 一句话：** RadarDistill 通过 CMA、AFD 和 PFD 将 LiDAR 特征的有效属性选择性迁移到雷达表征，在 nuScenes 纯雷达检测上达到 20.5% mAP 和 43.7% NDS。
- **任务：** 任务是在 nuScenes 上利用训练期 LiDAR 特征增强噪声大且稀疏的雷达表示，执行纯雷达三维目标检测，并检验其对 Camera-Radar 融合模型的增益。
- **Argue 点：** 作者主张，有针对性地对齐模态并只在高激活区域和目标候选区域蒸馏知识，比无差别迁移更能改善雷达检测表征。
- **核心创新：**
  - 提出由 Cross-Modality Alignment（CMA）、Activation-based Feature Distillation（AFD）和 Proposal-based Feature Distillation（PFD）组成的 RadarDistill。
  - CMA 以多层膨胀操作提高雷达特征密度，改善 LiDAR 到雷达的跨模态知识迁移。
  - AFD 聚焦超过预定义激活阈值的区域，PFD 则在目标候选区域内引导雷达网络模仿 LiDAR 特征。
- **解决的问题 / 故事：** 雷达数据稀疏且噪声较大，难以形成适合三维目标检测的有效表示。RadarDistill 先通过 CMA 缓解模态密度差异，再由 AFD 和 PFD 在信息更可靠的区域实施选择性蒸馏。该方法在 nuScenes 纯雷达任务上取得 20.5% mAP 和 43.7% NDS 的 SOTA 结果，并显著提升了 Camera-Radar 融合模型。

[CVF Open Access](https://openaccess.thecvf.com/content/CVPR2024/html/Bang_RadarDistill_Boosting_Radar-based_Object_Detection_Performance_via_Knowledge_Distillation_from_CVPR_2024_paper.html)

---

### 44. RadSimReal: Bridging the Gap Between Synthetic and Real Data in Radar Object Detection With Simulation

- **Scope：** `radar-perception`
- **TL;DR 一句话：** RadSimReal 无需真实数据或未公开的雷达设计细节即可生成带标注的合成雷达图像，并使检测器具备有竞争力的真实数据泛化性能。
- **任务：** 任务是针对不同雷达类型与环境条件合成带标注的雷达图像，用其训练目标检测模型，并在同域及跨真实数据集设置中评估。
- **Argue 点：** 作者主张，具备物理基础但不依赖雷达内部设计细节的仿真数据，能够替代难以采集和标注的真实雷达训练数据，并改善跨数据集泛化。
- **核心创新：**
  - 提出物理雷达仿真方法 RadSimReal，可在无需真实数据采集的情况下生成图像及其标注。
  - 支持多种雷达类型和环境条件，且不要求掌握供应商通常不公开的雷达设计细节。
  - 相较其他物理雷达仿真方法具有更快的运行速度。
- **解决的问题 / 故事：** 远距离、恶劣天气和复杂光照下的真实雷达数据难以采集与标注，制约了神经网络检测器训练。RadSimReal 以不依赖设备内部设计细节的物理仿真生成多条件合成雷达图像及标注。摘要报告，在合成数据上训练并于真实数据上测试的模型可媲美同一真实数据集内训练测试的模型，并在跨真实数据集测试时取得更好表现，但未给出具体数值。

[CVF Open Access](https://openaccess.thecvf.com/content/CVPR2024/html/Bialer_RadSimReal_Bridging_the_Gap_Between_Synthetic_and_Real_Data_in_CVPR_2024_paper.html)

---

### 45. RCBEVDet: Radar-camera Fusion in Bird's Eye View for 3D Object Detection

- **Scope：** `radar-perception`
- **TL;DR 一句话：** RCBEVDet 通过 RadarBEVNet 与 Cross-Attention Multi-layer Fusion 在 BEV 中对齐和融合雷达、相机特征，在 nuScenes 与 VoD 上取得 SOTA 且达到 21∼28 FPS。
- **任务：** 任务是输入多视角相机和毫米波雷达数据，在 nuScenes 与 view-of-delft（VoD）基准上实时输出三维目标检测结果。
- **Argue 点：** 作者主张，充分建模雷达点特征、RCS 尺寸先验及跨模态空间偏差，能够同时提升低成本 Radar-Camera 融合检测的精度、鲁棒性和速度。
- **核心创新：**
  - 提出 RadarBEVNet，以点编码器和 Transformer 编码器构成双流雷达骨干，并通过注入与提取模块交互信息。
  - 设计 RCS-aware BEV 编码器，将 Radar Cross-Section（RCS）作为目标尺寸先验用于 BEV 特征散布。
  - 提出 Cross-Attention Multi-layer Fusion，利用可变形注意力自动对齐多模态 BEV 特征，再进行通道与空间融合。
- **解决的问题 / 故事：** 纯相机方案成本低，但难以实现高精度、鲁棒的三维目标检测，而 Radar-Camera 融合仍需解决雷达表示与模态对齐问题。RCBEVDet 用 RadarBEVNet 提取融合点级、Transformer 与 RCS 先验的雷达特征，再以跨注意力完成 BEV 对齐和融合。其在 nuScenes 和 VoD 上取得新的 Radar-Camera 融合 SOTA，并以 21∼28 FPS 超过所有实时纯相机及 Radar-Camera 三维检测器。

[CVF Open Access](https://openaccess.thecvf.com/content/CVPR2024/html/Lin_RCBEVDet_Radar-camera_Fusion_in_Birds_Eye_View_for_3D_Object_CVPR_2024_paper.html)

---

### 46. SIRA: Scalable Inter-frame Relation and Association for Radar Perception

- **Scope：** `radar-perception`
- **TL;DR 一句话：** SIRA 通过可扩展的多跨帧时序关系建模和运动一致性伪轨迹关联，显著提升雷达有向目标检测与多目标跟踪性能。
- **任务：** 任务是在 Radiate 数据集的自车视角雷达序列中进行有向目标检测和多目标跟踪，并处理非线性运动、噪声、鬼影及运动模糊。
- **Argue 点：** 作者主张，跨越更长时间范围建模特征关系并以空间运动一致性约束目标关联，是克服雷达感知缺陷的关键。
- **核心创新：**
  - 提出 Scalable Inter-frame Relation and Association（SIRA）框架。
  - 受 Swin Transformer 启发，以时间重组的窗口注意力将两连续帧关系扩展到多个跨帧。
  - 提出 motion consistency track，利用观测数据生成 pseudo-tracklet，以改进轨迹预测与后续目标关联。
- **解决的问题 / 故事：** 传统雷达感知受低空间分辨率、噪声、多径、幽灵目标和运动模糊影响，在自车视角下还会因非线性运动进一步恶化。SIRA 将时序关系从相邻两帧扩展到多个跨帧，并用伪轨迹片段强化运动一致性关联。它在 Radiate 上取得 58.11 mAP@0.5 和 47.79 MOTA，分别较此前 SOTA 提升 +4.11 mAP@0.5 和 +9.94 MOTA。

[CVF Open Access](https://openaccess.thecvf.com/content/CVPR2024/html/Yataka_SIRA_Scalable_Inter-frame_Relation_and_Association_for_Radar_Perception_CVPR_2024_paper.html)

---

### 47. Towards Robust 3D Object Detection with LiDAR and 4D Radar Fusion in Various Weather Conditions

- **Scope：** `rf-wireless-sensing`
- **TL;DR 一句话：** 该框架以 3D-LRF 和天气条件雷达流门控网络融合 LiDAR 与 4D Radar，在不同正常及恶劣天气下实现鲁棒的三维目标检测。
- **任务：** 任务是输入 LiDAR 与 4D Radar 的三维观测，在多种正常和恶劣天气条件下定位并检测三维目标。
- **Argue 点：** 作者主张，融合时显式考虑两类传感器的三维空间特性与当前天气，并动态调节雷达信息流，才能充分结合 LiDAR 和 4D Radar 的互补优势。
- **核心创新：**
  - 提出 3D-LRF 模块，根据 LiDAR 与 4D Radar 在三维空间中的不同模式和空间关系提取融合特征。
  - 提出 weather-conditional radar-flow gating network，依据天气条件调节融合特征中的信息流。
  - 保留并利用既有融合方法容易丢失的高度信息，以辅助三维目标定位。
- **解决的问题 / 故事：** 既有 LiDAR 与 4D Radar 融合方法往往忽略传感器特性和天气差异，还会损失有助于目标定位的高度信息。该方法通过 3D-LRF 建模 LiDAR 的精确三维测绘与 4D Radar 的大范围全天候测量，再用天气条件门控动态组合二者。摘要报告模型在各种天气条件下取得三维目标检测 SoTA 性能，但未给出数据集、指标或具体数值。

[CVF Open Access](https://openaccess.thecvf.com/content/CVPR2024/html/Chae_Towards_Robust_3D_Object_Detection_with_LiDAR_and_4D_Radar_CVPR_2024_paper.html)

---

### 48. TransLoc4D: Transformer-based 4D Radar Place Recognition

- **Scope：** `radar-perception`
- **TL;DR 一句话：** TransLoc4D 结合 Minkloc4D 稀疏卷积骨干与 Transformer，利用 4D Radar 的几何、强度和速度信息实现面向动态及恶劣环境的地点识别。
- **任务：** 任务是根据稀疏且含噪的 4D Radar 扫描生成地点描述特征，并在作者构建的两个数据集和基准上完成地点识别。
- **Argue 点：** 作者主张，4D Radar 的强度与速度信息能够补充几何结构，而长程自注意力可缓解点云稀疏和噪声，从而支持恶劣天气下的鲁棒地点识别。
- **核心创新：**
  - 提出基于稀疏卷积和 Transformer 的 4D Radar 地点识别模型 TransLoc4D。
  - 设计 Minkloc4D 骨干网络，联合利用 4D Radar 的几何、强度和速度属性。
  - 构建两个数据集并建立 4D Radar 地点识别基准。
- **解决的问题 / 故事：** 相机和 3D LiDAR 地点识别方法在雨雾中可能退化，而 4D 毫米波 Radar 更少受到微小雨滴和雾滴干扰。TransLoc4D 用 Minkloc4D 提取几何、强度和速度特征，并通过线性自注意力捕获长程依赖以缓解稀疏与噪声。摘要报告两个新建基准上的实验验证了方法可行性及其应对动态和恶劣环境的鲁棒性，但未提供具体指标。

[CVF Open Access](https://openaccess.thecvf.com/content/CVPR2024/html/Peng_TransLoc4D_Transformer-based_4D_Radar_Place_Recognition_CVPR_2024_paper.html)

---

### 49. Unleashing Channel Potential: Space-Frequency Selection Convolution for SAR Object Detection

- **Scope：** `sar-remote-sensing`
- **TL;DR 一句话：** SFS-Conv 以空间-频率分流、感知和选择提升单层特征多样性，由此构建的 SFS-CNet 在降低模型规模与计算成本的同时改进 SAR 目标检测性能。
- **任务：** 任务是输入合成孔径雷达（SAR）图像进行目标检测，并在一系列 SAR 基准上同时评估检测性能、模型规模和计算成本。
- **Argue 点：** 作者主张，与压缩既有模型或直接设计轻量网络相比，在卷积层内部减少冗余并保留互补的空间和频率信息，可以更好地兼顾精度与效率。
- **核心创新：**
  - 提出采用分流-感知-选择策略的高效卷积模块 SFS-Conv。
  - 空间分支动态调整感受野以感知目标上下文，频率分支通过 fractional Gabor transformer 捕获频率变化和纹理特征。
  - 设计无参数特征选择模块自适应融合两类特征，并据此构建轻量网络 SFS-CNet。
- **解决的问题 / 故事：** DCNN 虽能有效检测 SAR 目标，但卷积层内的冗余特征造成巨大计算开销，而压缩或常规轻量化方案容易损失性能。SFS-Conv 将输入分为空间和频率分支分别提取上下文与纹理，再通过无参数模块保留最具代表性和区分度的信息。摘要报告 SFS-CNet 在一系列 SAR 检测基准上优于 SoTA，同时减少模型规模和计算成本，但未给出具体数值。

[CVF Open Access](https://openaccess.thecvf.com/content/CVPR2024/html/Li_Unleashing_Channel_Potential_Space-Frequency_Selection_Convolution_for_SAR_Object_Detection_CVPR_2024_paper.html)

---
