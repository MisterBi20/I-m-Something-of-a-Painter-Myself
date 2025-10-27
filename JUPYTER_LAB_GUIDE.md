# Jupyter Lab 环境配置

## 📋 环境要求

- Python 3.7+
- TensorFlow 2.8+
- Jupyter Lab
- GPU推荐（CPU也可以，但速度较慢）

## 🚀 安装步骤

### 1. 安装Python依赖

```bash
pip install -r requirements.txt
```

### 2. 安装Jupyter Lab

```bash
pip install jupyterlab
```

### 3. 启动Jupyter Lab

```bash
jupyter lab
```

## 📁 项目文件说明

### 核心文件
- `train_notebook.ipynb` - 完整的训练notebook（推荐使用）
- `kaggle_submit.ipynb` - Kaggle提交notebook
- `config.py` - 配置文件
- `data_loader.py` - 数据加载
- `models.py` - 模型定义
- `utils.py` - 工具函数

### 数据文件
- `data/Image_Generation_Data_Kaggle/` - 数据目录
  - `monet_tfrec/` - Monet TFRecord文件
  - `photo_tfrec/` - Photo TFRecord文件

## 🎯 使用流程

### 1. 训练模型
1. 打开 `train_notebook.ipynb`
2. 按顺序运行所有cells
3. 等待训练完成

### 2. 生成提交文件
1. 训练完成后会自动生成提交文件
2. 或者运行 `predict.py` 脚本

### 3. Kaggle提交
1. 将模型上传到Kaggle Dataset
2. 打开 `kaggle_submit.ipynb`
3. 修改MODEL_PATH变量
4. 运行所有cells

## ⚙️ 配置参数

在 `train_notebook.ipynb` 的第2个cell中修改参数：

```python
# 训练参数
BATCH_SIZE = 8          # 批次大小（根据显存调整）
EPOCHS = 20             # 训练轮数（推荐：20-50）
LEARNING_RATE = 2e-4    # 学习率

# 数据增强
USE_AUGMENTATION = True
AUGMENTATION_PROB = 0.5
```

## 🔧 常见问题

### Q: Jupyter Lab无法启动？
A: 检查Python环境，确保jupyterlab已安装

### Q: 训练过程中断？
A: 可以重新运行notebook，模型会自动保存checkpoint

### Q: 内存不足？
A: 减小BATCH_SIZE参数

### Q: GPU未使用？
A: 检查TensorFlow GPU安装，运行notebook中的GPU检查cell

## 📊 预期结果

- **训练时间**: 4-6小时（GPU）
- **FID Score**: ~40-50
- **生成图像**: 7000-10000张

## 🎉 完成！

现在你可以在Jupyter Lab中愉快地训练CycleGAN模型了！

**祝你竞赛成功！** 🎨🏆


