# I'm Something of a Painter Myself - Kaggle Competition

这是一个完整的Kaggle GAN竞赛解决方案，基于CycleGAN架构生成Monet风格的画作。

## 📋 目录

- [项目简介](#项目简介)
- [快速开始](#快速开始)
- [文件说明](#文件说明)
- [训练指南](#训练指南)
- [提交指南](#提交指南)
- [资源链接](#资源链接)

## 🎨 项目简介

**竞赛**: [Kaggle GAN Getting Started](https://www.kaggle.com/competitions/gan-getting-started)  
**任务**: 使用GAN生成7000-10000张Monet风格的画作  
**技术**: CycleGAN + 数据增强 + DiffAugmentation  
**评估**: FID (Fréchet Inception Distance)

本项目包含：
- ✅ 完整的CycleGAN实现
- ✅ 多种数据增强策略
- ✅ 一键训练脚本
- ✅ Kaggle提交notebook
- ✅ 详细的指南文档

## 🚀 快速开始

### 1. 环境设置

```bash
# 进入项目目录
cd Something-of-a-Painter

# 创建conda环境
conda env create -f environment.yml
conda activate autoformer

# 安装额外依赖
pip install opencv-python pillow tqdm
```

### 2. 准备数据

从Kaggle下载数据并解压到 `data/Image_Generation_Data_Kaggle/` 目录。

### 3. 开始训练

```bash
# 回到项目根目录
cd ..

# 快速测试（推荐初次使用）
chmod +x train_baseline.sh
./train_baseline.sh

# 或者平衡训练（推荐参赛）
chmod +x train_balanced.sh
./train_balanced.sh
```

### 4. 生成提交文件

```bash
# 使用训练好的模型生成图像
chmod +x predict.sh
./predict.sh <模型文件夹名称>
```

### 5. 提交到Kaggle

将生成的 `images.zip` 上传到竞赛页面。

**详细步骤请查看 [QUICK_START.md](QUICK_START.md)**

## 📁 文件说明

### 核心文件

```
I-m-Something-of-a-Painter-Myself/
├── README.md                          # 本文件
├── QUICK_START.md                     # 快速开始指南
├── COMPETITION_GUIDE.md               # 完整竞赛指南
├── kaggle_submission.ipynb           # Kaggle提交notebook
│
├── train_baseline.sh                  # 快速训练脚本
├── train_balanced.sh                 # 平衡训练脚本
├── train_best.sh                     # 最佳性能训练脚本
├── predict.sh                        # 预测脚本
│
└── Something-of-a-Painter/           # 原项目代码
    ├── models/                       # 模型定义
    ├── layers/                       # 网络层
    ├── exp/                          # 实验代码
    ├── data_provider/                # 数据加载
    └── utils/                        # 工具函数
```

### 文档说明

| 文件 | 说明 |
|------|------|
| `QUICK_START.md` | 5分钟快速上手指南 |
| `COMPETITION_GUIDE.md` | 完整的竞赛策略和技巧 |
| `kaggle_submission.ipynb` | Kaggle环境下的提交notebook |

### 训练脚本说明

| 脚本 | 特点 | 训练时间 | 适用场景 |
|------|------|----------|----------|
| `train_baseline.sh` | 快速测试 | ~1小时 | 初次使用、测试流程 |
| `train_balanced.sh` | 平衡性能 | ~4-6小时 | 竞赛推荐 |
| `train_best.sh` | 最佳性能 | ~12-24小时 | 追求最佳成绩 |

## 📚 训练指南

### 基础训练

```bash
python Something-of-a-Painter/run.py \
    --is_training 1 \
    --batch_size 8 \
    --train_epochs 20 \
    --steps_per_epoch -1 \
    --learning_rate 2e-4 \
    --model_id "EXPERIMENT_NAME"
```

### 使用数据增强

```bash
python Something-of-a-Painter/run.py \
    --is_training 1 \
    --diffaugment color translation cutout \
    --ds_augment \
    ...
```

### 监控训练

```bash
python Something-of-a-Painter/run.py \
    --is_training 1 \
    --wandb \
    ...
```

更多详细内容请查看 [COMPETITION_GUIDE.md](COMPETITION_GUIDE.md)

## 📤 提交指南

### 方法1: 使用本地训练的模型

1. 训练模型
2. 运行 `predict.sh` 生成图像
3. 下载 `images.zip`
4. 上传到Kaggle

### 方法2: 使用Kaggle Notebook

1. 将训练好的模型上传到Kaggle Dataset
2. 打开 `kaggle_submission.ipynb`
3. 修改 `MODEL_PATH` 变量
4. 运行所有cells
5. 下载 `images.zip` 并提交

## 🎯 提升成绩的技巧

1. **使用数据增强**: `--diffaugment color translation cutout`
2. **增加训练轮数**: `--train_epochs 50`
3. **调整batch size**: 根据显存调整 `--batch_size`
4. **监控训练**: 使用 `--wandb` 可视化训练过程
5. **多实验**: 尝试不同的超参数组合

## 📊 预期结果

| 配置 | FID Score | 训练时间 |
|------|-----------|----------|
| Baseline | ~50-60 | ~1小时 |
| + DiffAug | ~40-50 | ~4-6小时 |
| + 所有改进 | ~30-40 | ~12-24小时 |

## 🔗 资源链接

- **竞赛页面**: https://www.kaggle.com/competitions/gan-getting-started
- **原项目**: https://github.com/omerlux/Something-of-a-Painter
- **CycleGAN论文**: Zhu et al., Unpaired Image-to-Image Translation, ICCV 2017
- **DiffAug论文**: Zhao et al., Differentiable Augmentation for Data-Efficient GAN Training, NeurIPS 2020

## 💡 常见问题

### Q: 显存不足怎么办？
减小batch size: `--batch_size 1` 或 `--batch_size 2`

### Q: 训练很慢？
- 减少epochs
- 减少steps_per_epoch
- 使用更小的模型

### Q: 生成图像质量不好？
- 增加训练轮数
- 使用数据增强
- 调整学习率

### Q: 如何提交到Kaggle？
详见 [QUICK_START.md](QUICK_START.md) 中的提交步骤

## 📝 学习路径

1. **第一天**: 阅读指南、跑通baseline、理解流程
2. **第二-三天**: 尝试不同配置、优化超参数
3. **第四-五天**: 长时间训练最佳模型
4. **第六天**: 准备提交、测试、最终提交

## 🤝 贡献

本项目基于 [Something-of-a-Painter](https://github.com/omerlux/Something-of-a-Painter) 创建，增加了：
- 完整的竞赛指南
- 训练脚本
- Kaggle提交notebook
- 中文文档

## 📄 许可证

请查看原项目的 [LICENSE](Something-of-a-Painter/LICENSE) 文件。

## 🙏 致谢

- 感谢原项目作者 Orel Ben-Zaken 和 Omer Luxembourg
- Kaggle community 提供的支持和讨论

---

**祝你在竞赛中取得好成绩！** 🎨🏆
