# CycleGAN Monet风格转换项目

这是一个完整的Kaggle GAN竞赛解决方案，使用CycleGAN架构将照片转换为Monet风格的画作。

## 📁 项目结构

```
I-m-Something-of-a-Painter-Myself/
├── README.md                    # 项目说明
├── requirements.txt             # 依赖包
├── config.py                    # 配置文件
├── data_loader.py               # 数据加载
├── models.py                    # 模型定义
├── train.py                     # 训练脚本
├── predict.py                   # 预测脚本
├── utils.py                     # 工具函数
├── train_notebook.ipynb         # Jupyter训练notebook
├── kaggle_submit.ipynb         # Kaggle提交notebook
├── start.bat                   # Windows启动脚本
├── start.sh                    # Linux/Mac启动脚本
└── data/                       # 数据目录
    └── Image_Generation_Data_Kaggle/
        ├── monet_tfrec/        # Monet TFRecord文件
        └── photo_tfrec/        # Photo TFRecord文件
```

## 🚀 快速开始

### 方法1: 使用启动脚本

**Windows用户:**
```bash
start.bat
```

**Linux/Mac用户:**
```bash
./start.sh
```

### 方法2: Jupyter Lab (推荐)

```bash
# 安装依赖
pip install -r requirements.txt

# 启动Jupyter Lab
jupyter lab

# 打开 train_notebook.ipynb
```

### 方法3: 命令行

```bash
# 安装依赖
pip install -r requirements.txt

# 训练模型
python train.py

# 生成提交文件
python predict.py
```

## 📊 数据说明

- **Monet图像**: 300张Monet原画
- **Photo图像**: 7038张照片
- **格式**: TFRecord文件，256x256像素

## ⚙️ 配置参数

主要参数在 `config.py` 中：

```python
BATCH_SIZE = 8          # 批次大小
EPOCHS = 20             # 训练轮数
LEARNING_RATE = 2e-4    # 学习率
```

## 🎯 预期结果

- **FID Score**: ~40-50
- **训练时间**: 4-6小时（GPU）
- **生成图像**: 7000-10000张

## 🏆 Kaggle提交

### 本地提交
1. 运行 `python predict.py`
2. 上传生成的 `submission.zip` 文件

### Kaggle平台提交
1. 将模型上传到Kaggle Dataset
2. 打开 `kaggle_submit.ipynb`
3. 修改MODEL_PATH变量
4. 运行所有cells

## 🔧 常见问题

**Q: 训练速度很慢？**
A: 确保使用GPU，调整BATCH_SIZE

**Q: 生成质量不好？**
A: 增加训练轮数，调整学习率

**Q: 内存不足？**
A: 减小BATCH_SIZE

## 📚 详细使用

详细使用说明请查看 `train_notebook.ipynb` 中的注释。

---

**祝你竞赛成功！** 🎨🏆


