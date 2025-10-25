#!/bin/bash
# Balanced Training Script - Good Performance with Reasonable Time
# Recommended for most users

echo "=========================================="
echo "Balanced Training - Best for Competition"
echo "=========================================="
echo ""

cd Something-of-a-Painter

python run.py \
    --is_training 1 \
    --batch_size 8 \
    --train_epochs 20 \
    --steps_per_epoch -1 \
    --learning_rate 2e-4 \
    --diffaugment color translation cutout \
    --model_id "BALANCED" \
    --data "IGDK" \
    --root_path "../../data/Image_Generation_Data_Kaggle/"

echo ""
echo "=========================================="
echo "Training completed!"
echo "Check saves/ folder for results"
echo "=========================================="


