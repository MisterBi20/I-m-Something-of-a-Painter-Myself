"""
工具函数
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from PIL import Image
import shutil

def discriminator_loss(real, generated):
    """判别器损失函数"""
    real_loss = tf.keras.losses.BinaryCrossentropy(from_logits=True, reduction=tf.keras.losses.Reduction.NONE)(
        tf.ones_like(real), real)
    generated_loss = tf.keras.losses.BinaryCrossentropy(from_logits=True, reduction=tf.keras.losses.Reduction.NONE)(
        tf.zeros_like(generated), generated)
    total_disc_loss = real_loss + generated_loss
    return total_disc_loss * 0.5

def generator_loss(generated):
    """生成器损失函数"""
    return tf.keras.losses.BinaryCrossentropy(from_logits=True, reduction=tf.keras.losses.Reduction.NONE)(
        tf.ones_like(generated), generated)

def calc_cycle_loss(real_image, cycled_image, LAMBDA):
    """循环一致性损失"""
    loss1 = tf.reduce_mean(tf.abs(real_image - cycled_image))
    return LAMBDA * loss1

def identity_loss(real_image, same_image, LAMBDA):
    """恒等损失"""
    loss = tf.reduce_mean(tf.abs(real_image - same_image))
    return LAMBDA * 0.5 * loss

def display_samples(dataset, num_samples=8, title="Samples"):
    """显示样本图像"""
    fig, axes = plt.subplots(2, 4, figsize=(12, 6))
    axes = axes.ravel()
    
    for i, (monet, photo) in enumerate(dataset.take(num_samples)):
        if i >= 8:
            break
            
        # 显示Monet图像
        axes[i].imshow(monet[0] * 0.5 + 0.5)
        axes[i].set_title(f'Monet {i+1}')
        axes[i].axis('off')
    
    plt.suptitle(title)
    plt.tight_layout()
    plt.show()

def display_generated_samples(photo_dataset, generator, num_samples=8):
    """显示生成的样本"""
    fig, axes = plt.subplots(2, 8, figsize=(16, 4))
    
    for i, photo in enumerate(photo_dataset.take(num_samples)):
        if i >= 8:
            break
            
        # 原始照片
        axes[0, i].imshow(photo[0] * 0.5 + 0.5)
        axes[0, i].set_title(f'Original {i+1}')
        axes[0, i].axis('off')
        
        # 生成的Monet风格
        generated = generator(photo, training=False)
        axes[1, i].imshow(generated[0] * 0.5 + 0.5)
        axes[1, i].set_title(f'Generated {i+1}')
        axes[1, i].axis('off')
    
    plt.suptitle('Photo to Monet Style Transfer')
    plt.tight_layout()
    plt.show()

def save_samples(photo_dataset, generator, save_dir, num_samples=10):
    """保存样本图像"""
    os.makedirs(save_dir, exist_ok=True)
    
    for i, photo in enumerate(photo_dataset.take(num_samples)):
        # 生成Monet风格图像
        generated = generator(photo, training=False)
        
        # 转换为PIL图像并保存
        img_array = (generated[0].numpy() * 127.5 + 127.5).astype(np.uint8)
        img = Image.fromarray(img_array)
        img.save(os.path.join(save_dir, f'sample_{i+1}.jpg'))
    
    print(f"已保存 {num_samples} 个样本到 {save_dir}")

def predict_and_save(photo_dataset, generator, output_dir):
    """生成并保存所有提交图像"""
    os.makedirs(output_dir, exist_ok=True)
    
    print("正在生成提交图像...")
    count = 0
    
    for photo in photo_dataset:
        # 生成Monet风格图像
        generated = generator(photo, training=False)
        
        # 转换为PIL图像并保存
        img_array = (generated[0].numpy() * 127.5 + 127.5).astype(np.uint8)
        img = Image.fromarray(img_array)
        img.save(os.path.join(output_dir, f'{count+1}.jpg'))
        
        count += 1
        
        if count % 100 == 0:
            print(f"已生成 {count} 张图像")
    
    print(f"总共生成了 {count} 张图像")
    
    # 创建ZIP文件
    zip_path = shutil.make_archive(output_dir, 'zip', output_dir)
    zip_size = os.path.getsize(zip_path) / (1024 * 1024)
    
    print(f"ZIP文件已创建: {zip_path}")
    print(f"文件大小: {zip_size:.2f} MB")
    
    return count

class LogCallback(tf.keras.callbacks.Callback):
    """训练日志回调"""
    
    def __init__(self, log_interval=100):
        super().__init__()
        self.log_interval = log_interval
    
    def on_batch_end(self, batch, logs=None):
        if batch % self.log_interval == 0:
            print(f"Batch {batch}: "
                  f"Monet Gen Loss: {logs['monet_gen_loss']:.4f}, "
                  f"Photo Gen Loss: {logs['photo_gen_loss']:.4f}, "
                  f"Monet Disc Loss: {logs['monet_disc_loss']:.4f}, "
                  f"Photo Disc Loss: {logs['photo_disc_loss']:.4f}, "
                  f"Cycle Loss: {logs['total_cycle_loss']:.4f}")

def plot_training_history(history):
    """绘制训练历史"""
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    
    # Generator Loss
    axes[0, 0].plot(history.history['monet_gen_loss'], label='Monet Gen')
    axes[0, 0].plot(history.history['photo_gen_loss'], label='Photo Gen')
    axes[0, 0].set_title('Generator Loss')
    axes[0, 0].set_xlabel('Epoch')
    axes[0, 0].set_ylabel('Loss')
    axes[0, 0].legend()
    axes[0, 0].grid(True)
    
    # Discriminator Loss
    axes[0, 1].plot(history.history['monet_disc_loss'], label='Monet Disc')
    axes[0, 1].plot(history.history['photo_disc_loss'], label='Photo Disc')
    axes[0, 1].set_title('Discriminator Loss')
    axes[0, 1].set_xlabel('Epoch')
    axes[0, 1].set_ylabel('Loss')
    axes[0, 1].legend()
    axes[0, 1].grid(True)
    
    # Cycle Loss
    axes[1, 0].plot(history.history['total_cycle_loss'], label='Cycle Loss')
    axes[1, 0].set_title('Cycle Consistency Loss')
    axes[1, 0].set_xlabel('Epoch')
    axes[1, 0].set_ylabel('Loss')
    axes[1, 0].legend()
    axes[1, 0].grid(True)
    
    # Combined Loss
    axes[1, 1].plot(history.history['monet_gen_loss'], label='Monet Gen')
    axes[1, 1].plot(history.history['photo_gen_loss'], label='Photo Gen')
    axes[1, 1].plot(history.history['monet_disc_loss'], label='Monet Disc')
    axes[1, 1].plot(history.history['photo_disc_loss'], label='Photo Disc')
    axes[1, 1].set_title('All Losses')
    axes[1, 1].set_xlabel('Epoch')
    axes[1, 1].set_ylabel('Loss')
    axes[1, 1].legend()
    axes[1, 1].grid(True)
    
    plt.tight_layout()
    plt.show()

