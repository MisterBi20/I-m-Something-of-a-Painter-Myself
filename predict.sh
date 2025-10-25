#!/bin/bash
# Prediction Script - Generate images for submission
# Usage: ./predict.sh <model_folder_name>

if [ -z "$1" ]; then
    echo "Usage: ./predict.sh <model_folder_name>"
    echo "Example: ./predict.sh IGDK-CycleGan-EXP-bs16-monetos-noaug-20220628-221349"
    exit 1
fi

MODEL_FOLDER=$1

echo "=========================================="
echo "Generating Submission Images"
echo "Model: $MODEL_FOLDER"
echo "=========================================="
echo ""

cd Something-of-a-Painter

python run.py \
    --is_training 0 \
    --save "$MODEL_FOLDER" \
    --do_predict \
    --data "IGDK" \
    --root_path "../../data/Image_Generation_Data_Kaggle/"

echo ""
echo "=========================================="
echo "Prediction completed!"
echo "Check saves/$MODEL_FOLDER/images.zip"
echo "=========================================="

