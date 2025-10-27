#!/bin/bash

# CycleGAN Monet Style Transfer - Jupyter Lab Setup

echo "🎨 CycleGAN Monet Style Transfer Project"
echo "========================================"

# Check Python environment
if ! command -v python &> /dev/null; then
    echo "❌ Python not installed, please install Python 3.7+"
    exit 1
fi

# Check data directory
if [ ! -d "data/Image_Generation_Data_Kaggle" ]; then
    echo "❌ Data directory not found"
    echo "Please ensure data is placed in data/Image_Generation_Data_Kaggle/ directory"
    exit 1
fi

echo "✅ Environment check passed"

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Dependency installation failed"
    exit 1
fi

echo "✅ Dependencies installed successfully"

# Install Jupyter Lab if not installed
echo "📓 Checking Jupyter Lab..."
if ! command -v jupyter &> /dev/null; then
    echo "Installing Jupyter Lab..."
    pip install jupyterlab
fi

echo "✅ Jupyter Lab ready"

# Start Jupyter Lab
echo "🚀 Starting Jupyter Lab..."
echo "Please open train_notebook.ipynb to start training"
echo "========================================"

jupyter lab


