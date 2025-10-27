"""
预测脚本 - 生成Kaggle提交文件
"""

import os
import argparse
import tensorflow as tf
from config import Config
from data_loader import create_predict_dataset
from models import Generator
from utils import predict_and_save

def main():
    """主预测函数"""
    parser = argparse.ArgumentParser(description='生成Kaggle提交文件')
    parser.add_argument('--model_path', type=str, default=None,
                        help='模型路径（如果不指定，使用最新的模型）')
    parser.add_argument('--output_dir', type=str, default='submission',
                        help='输出目录')
    
    args = parser.parse_args()
    
    print("🎨 生成Kaggle提交文件")
    print("=" * 50)
    
    # 查找模型文件
    if args.model_path is None:
        # 查找最新的模型
        saves_dir = Config.SAVE_DIR
        if not os.path.exists(saves_dir):
            print(f"❌ 保存目录不存在: {saves_dir}")
            print("请先运行 python train.py 训练模型")
            return
        
        # 获取最新的模型目录
        model_dirs = [d for d in os.listdir(saves_dir) if d.startswith(Config.MODEL_NAME)]
        if not model_dirs:
            print(f"❌ 未找到模型目录")
            print("请先运行 python train.py 训练模型")
            return
        
        latest_model_dir = sorted(model_dirs)[-1]
        model_path = os.path.join(saves_dir, latest_model_dir, "monet_generator.h5")
    else:
        model_path = args.model_path
    
    # 检查模型文件是否存在
    if not os.path.exists(model_path):
        print(f"❌ 模型文件不存在: {model_path}")
        return
    
    print(f"📁 使用模型: {model_path}")
    
    # 加载模型
    print("🔄 加载模型...")
    try:
        monet_generator = tf.keras.models.load_model(model_path)
        print("✅ 模型加载成功")
    except Exception as e:
        print(f"❌ 模型加载失败: {e}")
        return
    
    # 创建预测数据集
    print("📁 加载数据...")
    photo_dataset = create_predict_dataset()
    
    # 生成图像
    print("🎨 生成Monet风格图像...")
    count = predict_and_save(photo_dataset, monet_generator, args.output_dir)
    
    # 验证结果
    print("\n📊 结果验证:")
    print(f"生成图像数量: {count}")
    
    if count < 7000:
        print("⚠️ 警告: 图像数量少于7000张！")
    elif count > 10000:
        print("⚠️ 警告: 图像数量超过10000张！")
    else:
        print("✅ 图像数量符合要求 (7000-10000张)")
    
    print(f"\n🎉 提交文件已生成: {args.output_dir}.zip")
    print("请将此文件上传到Kaggle竞赛页面")

if __name__ == "__main__":
    main()


