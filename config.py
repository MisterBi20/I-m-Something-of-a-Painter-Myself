"""
配置文件 - 训练参数设置
"""

import os

class Config:
    """训练配置类"""
    
    # ========== 数据路径 ==========
    DATA_ROOT = "data/Image_Generation_Data_Kaggle"
    MONET_TFREC_PATH = os.path.join(DATA_ROOT, "monet_tfrec")
    PHOTO_TFREC_PATH = os.path.join(DATA_ROOT, "photo_tfrec")
    
    # ========== 模型参数 ==========
    IMAGE_SIZE = 256
    CHANNELS = 3
    LAMBDA_CYCLE = 10.0
    LAMBDA_IDENTITY = 0.5
    
    # ========== 训练参数 ==========
    BATCH_SIZE = 8
    EPOCHS = 20
    LEARNING_RATE = 2e-4
    BETA_1 = 0.5
    
    # ========== 数据增强 ==========
    USE_AUGMENTATION = True
    AUGMENTATION_PROB = 0.5
    
    # ========== 保存路径 ==========
    SAVE_DIR = "saves"
    MODEL_NAME = "cyclegan_monet"
    
    # ========== 其他设置 ==========
    SEED = 42
    VERBOSE = 1
    SAVE_SAMPLES = True
    NUM_SAMPLES_TO_SAVE = 10
    
    # ========== Kaggle提交 ==========
    SUBMISSION_IMAGES_COUNT = 7038  # 生成与输入照片相同数量的图像
    
    @classmethod
    def print_config(cls):
        """打印配置信息"""
        print("=" * 50)
        print("训练配置:")
        print("=" * 50)
        print(f"数据路径: {cls.DATA_ROOT}")
        print(f"图像尺寸: {cls.IMAGE_SIZE}x{cls.IMAGE_SIZE}")
        print(f"批次大小: {cls.BATCH_SIZE}")
        print(f"训练轮数: {cls.EPOCHS}")
        print(f"学习率: {cls.LEARNING_RATE}")
        print(f"Cycle Loss权重: {cls.LAMBDA_CYCLE}")
        print(f"使用数据增强: {cls.USE_AUGMENTATION}")
        print("=" * 50)

