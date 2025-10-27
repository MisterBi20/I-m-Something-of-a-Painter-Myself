@echo off
chcp 65001 >nul

echo 🎨 CycleGAN Monet Style Transfer Project
echo ========================================

REM Check Python environment
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not installed, please install Python 3.7+
    pause
    exit /b 1
)

REM Check data directory
if not exist "data\Image_Generation_Data_Kaggle" (
    echo ❌ Data directory not found
    echo Please ensure data is placed in data\Image_Generation_Data_Kaggle\ directory
    pause
    exit /b 1
)

echo ✅ Environment check passed

REM Install dependencies
echo 📦 Installing dependencies...
pip install -r requirements.txt

if errorlevel 1 (
    echo ❌ Dependency installation failed
    pause
    exit /b 1
)

echo ✅ Dependencies installed successfully

REM Install Jupyter Lab if not installed
echo 📓 Checking Jupyter Lab...
jupyter --version >nul 2>&1
if errorlevel 1 (
    echo Installing Jupyter Lab...
    pip install jupyterlab
)

echo ✅ Jupyter Lab ready

REM Start Jupyter Lab
echo 🚀 Starting Jupyter Lab...
echo Please open train_notebook.ipynb to start training
echo ========================================

jupyter lab

pause


