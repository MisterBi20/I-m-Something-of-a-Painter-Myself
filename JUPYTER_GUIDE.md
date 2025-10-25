# Jupyter Lab 使用指南

## 📘 在Jupyter Lab中运行项目

本指南介绍如何在Jupyter Lab环境中运行和训练CycleGAN模型。

## 🚀 快速开始

### 1. 打开Notebook

```bash
# 启动Jupyter Lab
jupyter lab

# 在浏览器中打开 train_in_jupyter.ipynb
```

### 2. 配置数据路径

在 `train_in_jupyter.ipynb` 的第4个cell中，修改 `Config` 类：

```python
class Config:
    # 修改为你实际的数据路径
    root_path = 'D:/data/kaggle/'  # 改为你的路径
    
    # 其他参数保持不变或根据需求调整
    batch_size = 8
    train_epochs = 20
    # ...
```

**重要**：确保数据目录结构如下：
```
你的数据目录/
└── gan-getting-started/
    ├── monet_tfrec/
    │   ├── monet.tfrec-xxxxx
    │   └── ...
    └── photo_tfrec/
        ├── photo.tfrec-xxxxx
        └── ...
```

### 3. 运行所有Cells

按顺序运行所有cells：
- 右键点击notebook
- 选择 "Run All Cells"
- 或者按 `Shift + Enter` 逐个运行

## 📝 Notebook结构说明

### Cell 1: 导入库
- 导入所有必要的Python库
- 检查GPU是否可用
- 设置随机种子

### Cell 2: 配置参数 ⚠️ **需要修改**
- 配置数据路径 `root_path`
- 调整训练参数（batch_size, epochs等）
- 选择数据增强策略

### Cell 3: 加载数据
- 从TFRecord文件加载数据
- 显示数据统计信息
- 自动计算训练步数

### Cell 4: 可视化数据样本
- 显示Monet和Photo样本
- 验证数据加载是否正确

### Cell 5: 构建模型
- 创建生成器和判别器
- 显示模型参数量

### Cell 6: 配置优化器
- 设置Adam优化器
- 配置学习率

### Cell 7: 创建并编译CycleGAN
- 创建完整的CycleGAN模型
- 编译模型准备训练

### Cell 8: 开始训练 ⏱️ **最耗时**
- 训练模型
- 显示训练进度
- 可能需要数小时

### Cell 9: 可视化训练损失
- 绘制loss曲线
- 分析训练效果

### Cell 10: 可视化生成结果
- 显示生成的Monet风格图像
- 评估生成质量

### Cell 11: 保存模型
- 保存训练好的模型
- 保存checkpoint

### Cell 12: 生成提交文件
- 生成所有提交图像
- 创建ZIP文件
- 验证文件数量

## ⚙️ 配置参数说明

### 基本参数

| 参数 | 说明 | 推荐值 |
|------|------|--------|
| `root_path` | 数据根目录 | 你的数据路径 |
| `batch_size` | 批次大小 | 4/8/16（根据显存） |
| `train_epochs` | 训练轮数 | 20-50 |
| `learning_rate` | 学习率 | 2e-4 |

### 数据增强参数

```python
# 数据集增强（训练前增强）
ds_augment = False  # True/False

# DiffAugmentation（训练中增强）
diffaugment = ['color', 'translation', 'cutout']
```

### 模型参数

```python
height = 256          # 图像高度
width = 256           # 图像宽度
channels = 3          # RGB通道
lambda_cycle = 10     # Cycle Loss权重
```

## 💡 使用技巧

### 1. 快速测试
- 设置 `train_epochs = 3`
- 设置 `batch_size = 4`
- 验证流程是否正确

### 2. 完整训练
- 设置 `train_epochs = 20`
- 设置 `batch_size = 8`
- 使用 `diffaugment = ['color', 'translation', 'cutout']`

### 3. 最佳性能
- 设置 `train_epochs = 50`
- 设置 `batch_size = 16`
- 启用所有数据增强

## 🔧 常见问题

### Q1: 找不到数据文件
**原因**: 数据路径配置错误

**解决**: 
```python
# 检查路径
import os
os.path.exists('你的路径/gan-getting-started/monet_tfrec/')
```

### Q2: 显存不足（OOM）
**原因**: batch_size太大

**解决**: 
```python
batch_size = 1  # 减小到1或2
```

### Q3: 训练太慢
**原因**: 没有使用GPU

**解决**: 
- 检查Cell 1中是否检测到GPU
- 安装CUDA和cuDNN
- 安装GPU版本的TensorFlow

### Q4: 生成图像质量不好
**原因**: 训练轮数不足

**解决**: 
```python
train_epochs = 50  # 增加训练轮数
```

## 📊 监控训练

### 观察Loss变化
- Generator Loss 应该逐渐下降
- Discriminator Loss 应该波动但总体稳定
- Cycle Loss 应该逐渐减小

### 查看GPU使用率
```bash
# 新开一个终端
nvidia-smi -l 1
```

### 使用Jupyter的内置monitor
- 在Jupyter Lab顶部可以看到资源使用情况

## 🎯 推荐工作流程

### 第一次运行
1. 设置小规模的参数（epochs=3, batch_size=4）
2. 运行前几个cells验证数据加载
3. 运行训练cell查看是否报错
4. 逐步增加参数

### 正式训练
1. 设置完整的训练参数
2. 运行所有cells
3. 等待训练完成（数小时）
4. 查看结果和损失曲线
5. 生成提交文件

### 调优
1. 根据结果调整参数
2. 尝试不同的数据增强
3. 多次实验找到最佳配置

## 📁 输出文件说明

训练完成后，会在以下目录生成文件：

```
Something-of-a-Painter/saves/
└── EXP-20231201-120000/          # 时间戳文件夹
    ├── model_m_gen/              # 保存的模型
    ├── checkpoints/              # 训练checkpoint
    └── images/                   # 生成的图像
        ├── 1.jpg
        ├── 2.jpg
        └── ...
    └── images.zip                # 提交文件
```

## ✨ 高级技巧

### 1. 使用Wandb监控
```python
use_wandb = True  # 在配置中启用
# 需要先安装: pip install wandb
# 需要登录: wandb login
```

### 2. 继续训练
如果需要继续训练已保存的模型：
- 加载之前保存的checkpoint
- 修改epochs参数
- 重新运行训练cell

### 3. 调整学习率
```python
learning_rate = 1e-4  # 降低学习率进行精细调整
```

## 🎓 学习建议

1. **理解每个步骤**: 不要盲目运行，理解每个cell的作用
2. **观察变化**: 注意loss的变化和生成图像的质量
3. **多实验**: 尝试不同的参数组合
4. **保存结果**: 每次实验都要保存notebook和结果

## 📚 参考资源

- [CycleGAN论文](https://arxiv.org/abs/1703.10593)
- [Kaggle竞赛页面](https://www.kaggle.com/competitions/gan-getting-started)
- [TensorFlow文档](https://www.tensorflow.org/)

---

**祝你训练顺利！** 🎨

如有问题，请查看：
- QUICK_START.md - 快速开始指南
- COMPETITION_GUIDE.md - 完整竞赛指南
- README.md - 项目总览

