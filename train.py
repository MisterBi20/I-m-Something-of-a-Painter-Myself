"""
训练脚本 - CycleGAN Monet风格转换
"""

import os
import random
import numpy as np
import tensorflow as tf
from datetime import datetime

# 导入自定义模块
from config import Config
from data_loader import create_dataset
from models import Generator, Discriminator, CycleGAN
from utils import (
    discriminator_loss, generator_loss, calc_cycle_loss, identity_loss,
    display_samples, display_generated_samples, save_samples, plot_training_history,
    LogCallback
)

def set_seed(seed):
    """设置随机种子"""
    random.seed(seed)
    np.random.seed(seed)
    tf.random.set_seed(seed)

def main():
    """主训练函数"""
    print("🎨 CycleGAN Monet风格转换训练")
    print("=" * 50)
    
    # 设置随机种子
    set_seed(Config.SEED)
    
    # 打印配置
    Config.print_config()
    
    # 检查GPU
    gpus = tf.config.list_physical_devices('GPU')
    if gpus:
        print(f"✓ 检测到 {len(gpus)} 个GPU")
        try:
            for gpu in gpus:
                tf.config.experimental.set_memory_growth(gpu, True)
        except RuntimeError as e:
            print(f"GPU配置错误: {e}")
    else:
        print("⚠ 未检测到GPU，将使用CPU（速度会很慢）")
    
    # 创建保存目录
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    save_dir = os.path.join(Config.SAVE_DIR, f"{Config.MODEL_NAME}_{timestamp}")
    os.makedirs(save_dir, exist_ok=True)
    print(f"模型将保存到: {save_dir}")
    
    # 加载数据
    print("\n📁 加载数据...")
    dataset, n_monet, n_photo = create_dataset()
    
    # 显示数据样本
    print("\n🖼️ 显示数据样本...")
    display_samples(dataset, num_samples=8, title="Monet样本")
    
    # 创建模型
    print("\n🏗️ 创建模型...")
    monet_generator = Generator()
    photo_generator = Generator()
    monet_discriminator = Discriminator()
    photo_discriminator = Discriminator()
    
    print(f"生成器参数量: {monet_generator.count_params():,}")
    print(f"判别器参数量: {monet_discriminator.count_params():,}")
    
    # 创建优化器
    print("\n⚙️ 配置优化器...")
    monet_gen_optimizer = tf.keras.optimizers.Adam(Config.LEARNING_RATE, beta_1=Config.BETA_1)
    photo_gen_optimizer = tf.keras.optimizers.Adam(Config.LEARNING_RATE, beta_1=Config.BETA_1)
    monet_disc_optimizer = tf.keras.optimizers.Adam(Config.LEARNING_RATE, beta_1=Config.BETA_1)
    photo_disc_optimizer = tf.keras.optimizers.Adam(Config.LEARNING_RATE, beta_1=Config.BETA_1)
    
    # 创建CycleGAN模型
    cyclegan = CycleGAN(
        monet_generator=monet_generator,
        photo_generator=photo_generator,
        monet_discriminator=monet_discriminator,
        photo_discriminator=photo_discriminator,
        lambda_cycle=Config.LAMBDA_CYCLE
    )
    
    # 编译模型
    cyclegan.compile(
        m_gen_optimizer=monet_gen_optimizer,
        p_gen_optimizer=photo_gen_optimizer,
        m_disc_optimizer=monet_disc_optimizer,
        p_disc_optimizer=photo_disc_optimizer,
        gen_loss_fn=generator_loss,
        disc_loss_fn=discriminator_loss,
        cycle_loss_fn=calc_cycle_loss,
        identity_loss_fn=identity_loss
    )
    
    # 计算训练步数
    steps_per_epoch = max(n_monet, n_photo) // Config.BATCH_SIZE
    print(f"\n📊 训练配置:")
    print(f"每轮步数: {steps_per_epoch}")
    print(f"总步数: {steps_per_epoch * Config.EPOCHS}")
    
    # 开始训练
    print(f"\n🚀 开始训练...")
    print("=" * 50)
    
    # 创建回调
    callbacks = [
        LogCallback(log_interval=50),
        tf.keras.callbacks.ModelCheckpoint(
            filepath=os.path.join(save_dir, "checkpoint.h5"),
            save_weights_only=True,
            save_best_only=False,
            verbose=1
        )
    ]
    
    # 训练模型
    history = cyclegan.fit(
        dataset,
        steps_per_epoch=steps_per_epoch,
        epochs=Config.EPOCHS,
        verbose=Config.VERBOSE,
        callbacks=callbacks
    )
    
    print("\n✅ 训练完成！")
    
    # 保存模型
    print("\n💾 保存模型...")
    monet_generator.save(os.path.join(save_dir, "monet_generator.h5"))
    photo_generator.save(os.path.join(save_dir, "photo_generator.h5"))
    monet_discriminator.save(os.path.join(save_dir, "monet_discriminator.h5"))
    photo_discriminator.save(os.path.join(save_dir, "photo_discriminator.h5"))
    
    # 绘制训练历史
    print("\n📈 绘制训练历史...")
    plot_training_history(history)
    
    # 显示生成样本
    print("\n🎨 显示生成样本...")
    photo_dataset = dataset.map(lambda x, y: y)  # 提取photo部分
    display_generated_samples(photo_dataset, monet_generator, num_samples=8)
    
    # 保存样本
    if Config.SAVE_SAMPLES:
        print("\n💾 保存样本...")
        samples_dir = os.path.join(save_dir, "samples")
        save_samples(photo_dataset, monet_generator, samples_dir, Config.NUM_SAMPLES_TO_SAVE)
    
    print(f"\n🎉 训练完成！模型已保存到: {save_dir}")
    print("下一步: 运行 python predict.py 生成提交文件")

if __name__ == "__main__":
    main()


