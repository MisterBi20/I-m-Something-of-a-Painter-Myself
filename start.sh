#!/bin/bash

# CycleGAN Monet风格转换 - 启动脚本

echo "🎨 CycleGAN Monet风格转换项目"
echo "================================"

# 检查Python环境
if ! command -v python &> /dev/null; then
    echo "❌ Python未安装，请先安装Python 3.7+"
    exit 1
fi

# 检查数据目录
if [ ! -d "data/Image_Generation_Data_Kaggle" ]; then
    echo "❌ 数据目录不存在"
    echo "请确保数据已放在 data/Image_Generation_Data_Kaggle/ 目录"
    exit 1
fi

echo "✅ 环境检查通过"

# 安装依赖
echo "📦 安装依赖包..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ 依赖安装失败"
    exit 1
fi

echo "✅ 依赖安装完成"

# 选择运行方式
echo ""
echo "请选择运行方式："
echo "1. 命令行训练 (python train.py)"
echo "2. Jupyter Notebook (jupyter notebook)"
echo "3. 生成提交文件 (python predict.py)"
echo "4. 退出"
echo ""

read -p "请输入选择 (1-4): " choice

case $choice in
    1)
        echo "🚀 开始训练..."
        python train.py
        ;;
    2)
        echo "📓 启动Jupyter Notebook..."
        jupyter notebook
        ;;
    3)
        echo "🎨 生成提交文件..."
        python predict.py
        ;;
    4)
        echo "👋 再见！"
        exit 0
        ;;
    *)
        echo "❌ 无效选择"
        exit 1
        ;;
esac


