#!/bin/bash
# Best Training Script - Maximum Performance
# Uses all enhancements for best results

echo "=========================================="
echo "Best Training - Maximum Performance"
echo "=========================================="
echo ""

cd Something-of-a-Painter

python run.py \
    --is_training 1 \
    --batch_size 16 \
    --train_epochs 50 \
    --steps_per_epoch -1 \
    --learning_rate 2e-4 \
    --ds_augment \
    --diffaugment color translation cutout \
    --model_id "BEST" \
    --data "IGDK" \
    --root_path "../../data/Image_Generation_Data_Kaggle/" \
    --wandb

echo ""
echo "=========================================="
echo "Training completed!"
echo "Check saves/ folder for results"
echo "=========================================="


