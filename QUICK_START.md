# 快速开始指南

## 🚀 5分钟快速开始

### 前提条件
- Python 3.6+
- NVIDIA GPU (推荐) 或 CPU
- 已下载Kaggle竞赛数据

### 步骤1: 环境设置

```bash
# 进入项目目录
cd Something-of-a-Painter

# 创建环境（如果还没有）
conda env create -f environment.yml
conda activate autoformer

# 安装额外依赖
pip install opencv-python pillow tqdm
```

### 步骤2: 准备数据

将Kaggle数据解压到以下目录结构：
```
data/
└── Image_Generation_Data_Kaggle/
    ├── monet_jpg/
    ├── photo_jpg/
    ├── monet_tfrec/
    └── photo_tfrec/
```

### 步骤3: 开始训练

```bash
# 回到项目根目录
cd ..

# 方法1: 快速测试（5个epoch）
chmod +x train_baseline.sh
./train_baseline.sh

# 方法2: 平衡训练（推荐，20个epoch）
chmod +x train_balanced.sh
./train_balanced.sh

# 方法3: 最佳性能（50个epoch）
chmod +x train_best.sh
./train_best.sh
```

训练会在 `Something-of-a-Painter/saves/` 目录下创建模型文件夹。

### 步骤4: 生成提交文件

```bash
# 使用训练好的模型生成图像
chmod +x predict.sh
./predict.sh <你的模型文件夹名称>

# 例如：
./predict.sh IGDK-CycleGan-EXP-bs16-monetos-noaug-20220628-221349
```

生成的 `images.zip` 文件位于 `Something-of-a-Painter/saves/<模型文件夹>/images.zip`

### 步骤5: 提交到Kaggle

1. 下载 `images.zip`
2. 登录 Kaggle
3. 进入竞赛页面: https://www.kaggle.com/competitions/gan-getting-started
4. 点击 "Submit Predictions"
5. 上传 `images.zip`
6. 等待评估结果

## 📊 训练监控

如果安装了wandb，可以使用：

```bash
python Something-of-a-Painter/run.py \
    --is_training 1 \
    --wandb \
    --batch_size 8 \
    --train_epochs 20 \
    ...
```

然后在 https://wandb.ai 查看训练进度。

## 🔧 常见问题

### Q: 显存不足怎么办？
```bash
# 减小batch size
python Something-of-a-Painter/run.py --batch_size 1 ...
```

### Q: 训练很慢怎么办？
- 减少epochs: `--train_epochs 10`
- 减少steps: `--steps_per_epoch 200`
- 使用更少的增强

### Q: 生成图像质量不好？
- 增加训练轮数
- 使用数据增强
- 检查超参数

## 📝 下一步

- 阅读 [COMPETITION_GUIDE.md](COMPETITION_GUIDE.md) 了解详细策略
- 尝试不同的超参数组合
- 查看生成的图像示例
- 在Kaggle论坛学习其他方法

## 💡 提示

1. **先跑小规模测试**: 用 `train_baseline.sh` 确保流程正确
2. **保存每次实验**: 每个训练都会创建新的文件夹
3. **监控训练**: 如果使用wandb，及时发现问题
4. **多试几次**: GAN训练有随机性，尝试不同的random seed

祝你好运！🎨


