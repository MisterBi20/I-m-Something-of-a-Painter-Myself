@echo off
chcp 65001 >nul

echo 🎨 CycleGAN Monet风格转换项目
echo ================================

REM 检查Python环境
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python未安装，请先安装Python 3.7+
    pause
    exit /b 1
)

REM 检查数据目录
if not exist "data\Image_Generation_Data_Kaggle" (
    echo ❌ 数据目录不存在
    echo 请确保数据已放在 data\Image_Generation_Data_Kaggle\ 目录
    pause
    exit /b 1
)

echo ✅ 环境检查通过

REM 安装依赖
echo 📦 安装依赖包...
pip install -r requirements.txt

if errorlevel 1 (
    echo ❌ 依赖安装失败
    pause
    exit /b 1
)

echo ✅ 依赖安装完成

REM 选择运行方式
echo.
echo 请选择运行方式：
echo 1. Command Line Training (python train.py)
echo 2. Jupyter Notebook (jupyter notebook)
echo 3. Generate Submission (python predict.py)
echo 4. Exit
echo.

set /p choice="请输入选择 (1-4): "

if "%choice%"=="1" (
    echo 🚀 开始训练...
    python train.py
) else if "%choice%"=="2" (
    echo 📓 启动Jupyter Notebook...
    jupyter notebook
) else if "%choice%"=="3" (
    echo 🎨 生成提交文件...
    python predict.py
) else if "%choice%"=="4" (
    echo 👋 再见！
    exit /b 0
) else (
    echo ❌ 无效选择
    pause
    exit /b 1
)

pause
