# Kaggle GAN Getting Started 竞赛完整指南

## 竞赛概述

**竞赛名称**: I'm Something of a Painter Myself  
**竞赛链接**: https://www.kaggle.com/competitions/gan-getting-started  
**任务**: 使用GAN生成7000-10000张Monet风格的画作  
**评估指标**: 使用FID (Fréchet Inception Distance) 评估生成图像的质量

## 项目结构说明

这个项目使用**CycleGAN**架构来将照片转换为Monet风格的画作。CycleGAN的特点是不需要成对的训练数据，可以学习两个数据集之间的风格转换。

### 核心技术
1. **CycleGAN**: 无配对的图像到图像转换
2. **数据增强**: 提升模型泛化能力
3. **DiffAugmentation**: 可微分的增强策略
4. **双判别器**: 提升训练稳定性

## 完整实施步骤

### 第一步：环境和数据准备

#### 1. 本地环境设置（用于实验和调试）

```bash
# 进入项目目录
cd Something-of-a-Painter

# 创建conda环境
conda env create -f environment.yml
conda activate autoformer

# 安装额外依赖
pip install opencv-python pillow tqdm
```

#### 2. 下载Kaggle数据

```bash
# 方法1: 使用Kaggle API
pip install kaggle
kaggle competitions download -c gan-getting-started

# 方法2: 从Kaggle网站手动下载并解压到 data/ 目录
```

#### 3. 数据目录结构

```
data/
├── monet_jpg/          # Monet原画训练集
├── photo_jpg/          # 照片训练集
├── monet_tfrec/        # Monet TFRecord格式
└── photo_tfrec/        # Photo TFRecord格式
```

### 第二步：模型训练策略

#### 策略A：快速开始（推荐初学者）

**目标**: 快速跑通流程，获得可提交的结果

```bash
python run.py \
    --is_training 1 \
    --batch_size 4 \
    --train_epochs 5 \
    --steps_per_epoch 300 \
    --learning_rate 2e-4 \
    --model_id "BASELINE"
```

**配置说明**:
- 小batch size: 降低显存需求
- 少epochs: 快速迭代
- 少量steps: 快速验证流程

#### 策略B：平衡训练（推荐）

**目标**: 在时间和质量之间平衡

```bash
python run.py \
    --is_training 1 \
    --batch_size 8 \
    --train_epochs 20 \
    --steps_per_epoch -1 \
    --learning_rate 2e-4 \
    --diffaugment color translation cutout \
    --model_id "BALANCED"
```

**改进点**:
- 使用DiffAugmentation提升性能
- steps_per_epoch=-1 自动计算最佳步数
- 中等训练轮数

#### 策略C：高质量训练（追求最佳成绩）

**目标**: 最大化模型性能

```bash
python run.py \
    --is_training 1 \
    --batch_size 16 \
    --train_epochs 50 \
    --steps_per_epoch -1 \
    --learning_rate 2e-4 \
    --ds_augment \
    --diffaugment color translation cutout \
    --model_id "BEST" \
    --wandb
```

**高级特性**:
- Dataset Augmentation: 训练前数据增强
- DiffAugmentation: 训练中增强
- Wandb集成: 实时监控训练
- 更多训练轮数

### 第三步：Kaggle提交

#### 1. 修改 `submission-only.ipynb`

关键变量需要修改：
```python
# 第1个Cell中，修改为你训练好的模型路径
SAVE = "../input/YOUR-MODEL-PATH"
```

#### 2. 在Kaggle上传训练好的模型

- 将训练好的模型文件夹上传到Kaggle Dataset
- 确保路径正确

#### 3. 运行Notebook生成提交文件

- 打开Kaggle Notebook
- 添加数据源（数据和模型）
- 运行所有Cells
- 下载生成的 `images.zip`

#### 4. 提交到竞赛

- 从Kaggle Notebook下载 `images.zip`
- 上传到竞赛页面进行提交

## 提升成绩的技巧

### 1. 数据增强组合

项目包含两种增强方式：

**Dataset Augmentation** (`--ds_augment`):
- 翻转、旋转、裁剪
- 适用于CPU/GPU
- 注意：可能改变风格

**DiffAugmentation** (`--diffaugment`):
- Color, Translation, Cutout
- 可微分的增强
- 提升泛化能力

**推荐组合**: 只使用DiffAugmentation（颜色、平移、裁剪）

### 2. 超参数调优

关键超参数：

```python
--learning_rate: 2e-4     # 标准学习率
--batch_size: 8-16        # 根据显存调整
--train_epochs: 20-50     # 更多轮次通常更好
--lambda_cycle: 10        # Cycle loss权重（默认值）
```

### 3. 训练监控

使用Wandb监控训练：
```bash
python run.py --wandb --is_training 1 ...
```

监控关键指标：
- Generator Loss
- Discriminator Loss  
- Cycle Loss
- MiFID Score

### 4. 模型集成

训练多个模型并平均：
- 不同随机种子
- 不同超参数
- 不同数据增强

### 5. 后处理技巧

生成后可以尝试：
- 色彩饱和化
- 细节增强
- 边缘平滑

## 常见问题解决

### Q1: 显存不足 (OOM)

解决方案：
```bash
# 减小batch size
--batch_size 1

# 减少模型复杂度
# (修改layers/Generator.py中的滤波器数量)
```

### Q2: 训练不稳定

解决方案：
- 使用DiffAugmentation
- 调整学习率到1e-4
- 增加判别器训练频率

### Q3: 生成图像不够艺术化

解决方案：
- 增加训练轮数
- 调整Cycle Loss权重（减小lambda_cycle）
- 使用更多数据增强

### Q4: Kaggle提交错误

检查清单：
- [ ] 图像数量：7000-10000张
- [ ] 图像格式：JPEG
- [ ] 命名：1.jpg, 2.jpg, ...
- [ ] ZIP文件大小合理

## 实验建议

### 第一阶段：Baseline (1-2天)
- 跑通基础流程
- 生成初步结果
- 提交获得基准分数

### 第二阶段：优化 (3-5天)
- 尝试不同超参数
- 使用数据增强
- 监控训练过程

### 第三阶段：精炼 (2-3天)
- 微调模型
- 尝试集成
- 优化后处理

## 预期结果

根据项目README，使用改进的CycleGAN可以获得不错的成绩：
- Baseline: FID ~50-60
- 使用DiffAug: FID ~40-50
- 使用所有改进: FID ~30-40

## 实用资源

- **原项目论文**: Something-of-a-Painter/report.pdf
- **CycleGAN论文**: Zhu et al., 2017
- **DiffAug论文**: Zhao et al., 2020
- **Kaggle讨论区**: 查看其他选手的经验

## 时间规划

- **第1天**: 环境搭建、数据准备、运行baseline
- **第2-3天**: 尝试不同配置、优化超参数
- **第4-5天**: 长时间训练最佳模型
- **第6天**: 准备提交文件、测试、最终提交

## 祝竞赛顺利！

记住：
1. 先跑通baseline再优化
2. 保存每个实验的checkpoint
3. 多做实验，尝试不同配置
4. 关注Kaggle论坛学习其他方法
5. 保持耐心，GAN训练需要时间

