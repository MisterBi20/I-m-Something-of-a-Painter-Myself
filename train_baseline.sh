#!/bin/bash
# Baseline Training Script - Quick Start for Beginners
# This script runs a quick training to get familiar with the process

echo "=========================================="
echo "Baseline Training - Quick Start"
echo "=========================================="
echo ""

cd Something-of-a-Painter

python run.py \
    --is_training 1 \
    --batch_size 4 \
    --train_epochs 5 \
    --steps_per_epoch 300 \
    --learning_rate 2e-4 \
    --model_id "BASELINE" \
    --data "IGDK" \
    --root_path "../../data/Image_Generation_Data_Kaggle/"

echo ""
echo "=========================================="
echo "Training completed!"
echo "Check saves/ folder for results"
echo "=========================================="


