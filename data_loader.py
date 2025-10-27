"""
数据加载模块
"""

import os
import re
import numpy as np
import tensorflow as tf
from config import Config

def count_data_items(filenames):
    """计算TFRecord文件中的数据项数量"""
    n = [int(re.compile(r"-([0-9]*)\.").search(filename).group(1)) for filename in filenames]
    return np.sum(n)

def decode_image(image):
    """解码JPEG图像并归一化到[-1, 1]"""
    image = tf.image.decode_jpeg(image, channels=Config.CHANNELS)
    image = (tf.cast(image, tf.float32) / 127.5) - 1
    image = tf.reshape(image, [Config.IMAGE_SIZE, Config.IMAGE_SIZE, Config.CHANNELS])
    return image

def read_tfrecord(example):
    """读取TFRecord示例"""
    tfrecord_format = {
        'image_name': tf.io.FixedLenFeature([], tf.string),
        'image': tf.io.FixedLenFeature([], tf.string),
        'target': tf.io.FixedLenFeature([], tf.string)
    }
    example = tf.io.parse_single_example(example, tfrecord_format)
    image = decode_image(example['image'])
    return image

def load_dataset(filenames):
    """从TFRecord文件加载数据集"""
    dataset = tf.data.TFRecordDataset(filenames)
    dataset = dataset.map(read_tfrecord, num_parallel_calls=tf.data.AUTOTUNE)
    return dataset

def augment_image(image):
    """数据增强"""
    if not Config.USE_AUGMENTATION:
        return image
    
    # 随机水平翻转
    image = tf.image.random_flip_left_right(image)
    
    # 随机垂直翻转
    image = tf.image.random_flip_up_down(image)
    
    # 随机旋转（90度倍数）
    if tf.random.uniform([]) < Config.AUGMENTATION_PROB:
        k = tf.random.uniform([], 0, 4, dtype=tf.int32)
        image = tf.image.rot90(image, k)
    
    return image

def create_dataset():
    """创建训练数据集"""
    # 获取文件列表
    monet_files = tf.io.gfile.glob(os.path.join(Config.MONET_TFREC_PATH, "*.tfrec"))
    photo_files = tf.io.gfile.glob(os.path.join(Config.PHOTO_TFREC_PATH, "*.tfrec"))
    
    print(f"找到 {len(monet_files)} 个Monet TFRecord文件")
    print(f"找到 {len(photo_files)} 个Photo TFRecord文件")
    
    # 计算数据项数量
    n_monet = count_data_items(monet_files)
    n_photo = count_data_items(photo_files)
    
    print(f"Monet图像数量: {n_monet}")
    print(f"Photo图像数量: {n_photo}")
    
    # 加载数据集
    monet_ds = load_dataset(monet_files)
    photo_ds = load_dataset(photo_files)
    
    # 应用数据增强
    monet_ds = monet_ds.map(augment_image, num_parallel_calls=tf.data.AUTOTUNE)
    photo_ds = photo_ds.map(augment_image, num_parallel_calls=tf.data.AUTOTUNE)
    
    # 配置数据集
    monet_ds = monet_ds.shuffle(1000).repeat().batch(Config.BATCH_SIZE, drop_remainder=True)
    photo_ds = photo_ds.shuffle(1000).repeat().batch(Config.BATCH_SIZE, drop_remainder=True)
    
    # 缓存和预取
    monet_ds = monet_ds.cache().prefetch(tf.data.AUTOTUNE)
    photo_ds = photo_ds.cache().prefetch(tf.data.AUTOTUNE)
    
    # 创建配对数据集
    dataset = tf.data.Dataset.zip((monet_ds, photo_ds))
    
    return dataset, n_monet, n_photo

def create_predict_dataset():
    """创建预测数据集（用于生成提交文件）"""
    photo_files = tf.io.gfile.glob(os.path.join(Config.PHOTO_TFREC_PATH, "*.tfrec"))
    photo_ds = load_dataset(photo_files)
    photo_ds = photo_ds.batch(1)  # 单张图像批次
    return photo_ds

