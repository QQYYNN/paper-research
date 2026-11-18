[English README](../../README.md) · [中文 README](../../README.zh-CN.md) · [Walkthrough (EN)](README.md) · [全流程样例 (中文)](README.zh-CN.md)

# CVPR 2024 · 航空视觉 / Aerial vision

节选自历史调研文档 `paper-story-cards.md`。保留选中段落的原有卡片文字、编号和顺序。出版社摘要、摘要译文和本地文件路径经删节，论文链接可用于查阅原摘要。

Excerpt from the original `paper-story-cards.md` in the survey archive. Card notes, numbering, and order are preserved in Chinese. Publisher abstracts, their translations, and local paths are omitted. Follow the paper links for the abstracts.

## 原始卡片 / Original cards

### 1. Aerial Lifting: Neural Urban Semantic and Building Instance Lifting from Aerial Imagery

- **Scope：** `aerial-vision-peripheral`
- **TL;DR 一句话：** Aerial Lifting 利用 NeRF 将含噪二维标签提升至三维，以改善航空影像中的城市尺度语义分割与建筑级实例分割。
- **任务：** 输入多视角、不同飞行高度的城市航空影像及其含噪二维标签，输出三维一致的城市语义分割和建筑实例分割结果。
- **Argue 点：** 作者主张，联合利用跨高度标签信息、三维场景表示和重建深度先验，可以同时缓解尺度变化与多视图标签不一致问题，从而优于直接依赖二维标签的方法。
- **核心创新：**
  - 提出尺度自适应语义标签融合策略，借助 NeRF 的新视图合成能力融合不同高度预测的标签。
  - 提出基于三维场景表示的跨视图实例标签分组策略，以缓解二维实例标签的多视图不一致。
  - 利用多视图重建深度先验改善辐射场的几何质量，进而增强分割效果。
- **解决的问题 / 故事：** 城市航空影像中的建筑、汽车和道路尺度差异显著，而且单幅影像仅覆盖局部场景，导致现有二维标签存在分割困难和多视图不一致。Aerial Lifting 通过尺度自适应标签融合、跨视图实例分组和深度先验，将含噪二维标签提升到统一的三维表示中。多个真实城市尺度数据集上的实验表明，该方法优于现有方法，但摘要未给出具体提升数值。

[CVF Open Access](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_Aerial_Lifting_Neural_Urban_Semantic_and_Building_Instance_Lifting_from_CVPR_2024_paper.html)

---

### 2. Learnable Earth Parser: Discovering 3D Prototypes in Aerial Scans

- **Scope：** `aerial-vision-peripheral`
- **TL;DR 一句话：** Learnable Earth Parser 通过将大型航空 LiDAR 点云分解为少量可学习的三维原型，在无人工标注条件下实现可解释的场景解析。
- **任务：** 输入真实场景的大规模三维点云，学习原型形状并重建场景，同时支持无监督实例分割和小样本语义分割。
- **Argue 点：** 作者主张，基于概率重建学习少量三维形状原型，能够兼顾大型航空扫描的分解准确性、视觉可解释性和下游分割实用性。
- **核心创新：**
  - 构建概率重建模型，将输入三维点云分解为一小组学习得到的原型三维形状。
  - 以可解释的原型重建结果同时支持无监督实例分割和小样本语义分割。
  - 发布包含七个多样化真实场景大型航空 LiDAR 扫描的新数据集。
- **解决的问题 / 故事：** 航空测量与制图需要解析大规模三维扫描，但人工标注成本高，已有无监督方法也难以同时保证分解准确性与直观可解释性。Learnable Earth Parser 用概率重建模型发现少量三维原型，并以这些原型分解点云、支撑实例与语义分割。在包含七个大型航空 LiDAR 扫描的新数据集上，该方法的分解准确率优于当前最先进的无监督方法，同时保持了视觉可解释性。

[CVF Open Access](https://openaccess.thecvf.com/content/CVPR2024/html/Loiseau_Learnable_Earth_Parser_Discovering_3D_Prototypes_in_Aerial_Scans_CVPR_2024_paper.html)

---

### 3. Multiview Aerial Visual RECognition (MAVREC): Can Multi-view Improve Aerial Visual Perception?

- **Scope：** `aerial-vision-peripheral`
- **TL;DR 一句话：** MAVREC 以同步地面—无人机视频数据和半监督基准证明，使用同一地理位置的地面视角图像进行预训练能够增强航空目标检测。
- **任务：** 面向跨地理区域的航空目标检测，输入同步地面与无人机视角的有标签图像以及仅含航空视角的无标签图像，评估多视角预训练和半监督检测策略。
- **Argue 点：** 作者主张，地理位置匹配的地面视角数据能够为航空检测提供更有效的预训练信息，而联合有标签多视角数据与无标签航空数据可进一步提升检测能力。
- **核心创新：**
  - 发布 Multiview Aerial Visual RECognition（MAVREC）数据集，包含约 2.5 小时的 2.7K 同步视频、超过 50 万帧和 110 万个标注边界框。
  - 系统基准测试地面与航空多视角数据，发现同一地理位置的地面图像是更优的航空检测预训练资源。
  - 构建基于课程学习的半监督目标检测基准，联合有标签的地面与航空图像以及无标签的航空图像。
- **解决的问题 / 故事：** 现有 UAV 数据集往往规模较小、分辨率较低且地理与场景多样性不足，使主要由地面数据训练的 DNN 和开放世界基础模型难以适应航空视角。MAVREC 通过同步采集地面相机与无人机相机视频，为研究跨视角、跨地理位置的航空检测提供大规模数据。广泛基准测试表明，同地理位置地面图像增强预训练更有利于航空检测，并验证了课程式半监督方案的作用，但摘要未报告具体性能增幅。

[CVF Open Access](https://openaccess.thecvf.com/content/CVPR2024/html/Dutta_Multiview_Aerial_Visual_RECognition_MAVREC_Can_Multi-view_Improve_Aerial_Visual_CVPR_2024_paper.html)

---

### 4. SatSynth: Augmenting Image-Mask Pairs through Diffusion Models for Aerial Semantic Segmentation

- **Scope：** `aerial-vision-peripheral`
- **TL;DR 一句话：** SatSynth 通过扩散模型联合生成高质量且多样的卫星图像—掩码对，为标注稀缺条件下的航空语义分割提供有效的数据增强。
- **任务：** 学习卫星图像与语义标签的联合数据分布，生成相互对应的图像和分割掩码，并评估其对下游卫星影像语义分割训练的增益。
- **Argue 点：** 作者主张，联合生成而非仅生成图像或依赖判别式增强，可以同时保持细粒度质量与采样多样性，从而有效缓解地球观测语义分割的标注稀缺问题。
- **核心创新：**
  - 利用去噪扩散概率模型学习卫星图像与标签的联合数据流形。
  - 据作者所述，首次同时生成用于卫星影像分割的图像及其对应掩码，并兼顾细粒度质量和采样多样性。
  - 将生成的图像—掩码对用于下游分割增强，并与判别式扩散模型和 GAN 方法进行比较。
- **解决的问题 / 故事：** 卫星影像语义分割依赖大量专家标注，而地球观测类别在尺度和出现频率上的巨大差异又提高了数据增强难度。既有方法未能直接联合生成兼具细节质量与多样性的图像—掩码对，SatSynth 因此用扩散模型学习二者的联合数据流形。实验表明，加入生成样本相较基线及仅用原始数据训练均带来显著定量提升，但摘要未提供具体数值。

[CVF Open Access](https://openaccess.thecvf.com/content/CVPR2024/html/Toker_SatSynth_Augmenting_Image-Mask_Pairs_through_Diffusion_Models_for_Aerial_Semantic_CVPR_2024_paper.html)

---

### 5. View-decoupled Transformer for Person Re-identification under Aerial-ground Camera Network

- **Scope：** `aerial-vision-peripheral`
- **TL;DR 一句话：** 视角解耦 Transformer（VDT）通过分离视角相关与视角无关特征，提升异构航空—地面相机网络中的行人重识别性能。
- **任务：** 输入航空相机与地面相机拍摄的行人图像，在巨大视角差异下进行跨相机身份匹配，并以 mAP 和 Rank1 评估重识别性能。
- **Argue 点：** 作者主张，显式分离并约束视角相关和视角无关表征相互独立，可以减少视角差异对身份判别特征的干扰，且无需增加计算复杂度量级。
- **核心创新：**
  - 提出层次减法分离机制，在 VDT 内部分离视角相关特征与视角无关特征。
  - 设计正交损失，约束两类特征相互独立。
  - 发布大规模 CARGO 数据集，包含 5 台航空相机、8 台地面相机、5,000 个身份和 108,563 幅图像。
- **解决的问题 / 故事：** 现有行人重识别主要面向地面—地面等同构相机，剧烈的航空—地面视角差异会破坏身份判别表征。VDT 以层次减法分离和正交损失解耦视角相关与视角无关特征，并通过 CARGO 扩充 AGPReID 的评测基础。在相同量级计算复杂度下，VDT 相较先前方法在 CARGO 上的 mAP/Rank1 最高提升 5.0%/2.7%，在 AG-ReID 上最高提升 3.7%/5.2%。

[CVF Open Access](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_View-decoupled_Transformer_for_Person_Re-identification_under_Aerial-ground_Camera_Network_CVPR_2024_paper.html)

---

### 6. Weakly Misalignment-free Adaptive Feature Alignment for UAVs-based Multimodal Object Detection

- **Scope：** `uav-as-platform`
- **TL;DR 一句话：** 偏移引导自适应特征对齐（OAFA）通过估计 RGB-IR 特征偏移并面向检测任务自适应选择融合位置，提高 UAV 多模态目标检测对弱失配的鲁棒性。
- **任务：** 输入存在弱空间失配的 UAV 可见光—红外（RGB-IR）图像对，完成跨模态特征对齐、融合与目标检测。
- **Argue 点：** 作者主张，与忽略模态差异的严格对齐相比，在公共子空间估计特征偏移并以检测目标引导可变形融合，更能应对 RGB-IR 弱失配且降低严格对齐的实现负担。
- **核心创新：**
  - 提出 Offset-guided Adaptive Feature Alignment（OAFA），自适应调整多模态特征的相对位置。
  - 设计 Cross-modality Spatial Offset Modeling（CSOM）模块，在公共子空间中估计精确的特征级偏移。
  - 设计 Offset-guided Deformable Alignment and Fusion（ODAF）模块，隐式捕获适合检测任务的最优融合位置，而非执行严格对齐。
- **解决的问题 / 故事：** UAV RGB-IR 融合有助于目标检测，但图像对的弱失配会限制性能。现有方法往往忽略模态差异并追求严格对齐，既限制对齐质量，也增加实现成本。OAFA 通过 CSOM 建模跨模态偏移，再由 ODAF 面向检测任务进行可变形对齐与融合；实验报告其取得当前最先进的检测性能，并对弱失配表现出较强鲁棒性，但摘要未提供具体数值。

[CVF Open Access](https://openaccess.thecvf.com/content/CVPR2024/html/Chen_Weakly_Misalignment-free_Adaptive_Feature_Alignment_for_UAVs-based_Multimodal_Object_Detection_CVPR_2024_paper.html)

---

### 7. WildlifeMapper: Aerial Image Analysis for Multi-Species Detection and Identification

- **Scope：** `aerial-vision-peripheral`
- **TL;DR 一句话：** WildlifeMapper（WM）通过建模目标的局部结构与上下文，在多种景观的航空影像中实现多物种检测、定位和识别。
- **任务：** 输入不同国家与景观下的航空调查影像，输出多个野生动物物种的位置和类别，并以 mAP 评估检测性能与跨数据集泛化能力。
- **Argue 点：** 作者主张，充分捕获野生动物目标的局部结构及其上下文，可以克服同质化背景和局部结构表达不足造成的泛化限制，从而自动化多物种种群调查。
- **核心创新：**
  - 在 WildlifeMapper 中引入两个新模块，用于捕获目标的局部结构与上下文以改善定位和识别。
  - 发布大型航空影像数据集，包含超过 11k 幅图像和 28k 个经受训专家核验的标注。
  - 在来自 4 个国家的 3 个公开航空调查数据集上开展跨场景评估。
- **解决的问题 / 故事：** 传统野生动物种群评估劳动密集，而已有自动化方法受同质化背景和局部结构捕获不足影响，难以泛化到不同物种或景观。WildlifeMapper 通过两个新模块联合利用目标局部结构与上下文，并以专家核验的大型数据集支持训练和评估。该模型取得 0.56 mAP，并在来自 4 个国家的另外 3 个公开数据集上达到 SOTA，mAP 提升 42%。

[CVF Open Access](https://openaccess.thecvf.com/content/CVPR2024/html/Kumar_WildlifeMapper_Aerial_Image_Analysis_for_Multi-Species_Detection_and_Identification_CVPR_2024_paper.html)

---
