import os, shutil, random
import numpy as np

Postfix = 'jpg' # 里面都是jpg图片
BasePath = './datasets/seg_train' # 原图片和TXT文件
DatasetPath = './datasets/seg_data' # 保存的目标位置
ValSize, TestSize = 0.1, 0

os.makedirs(DatasetPath, exist_ok=True)
os.makedirs(f'{DatasetPath}/images', exist_ok=True)
os.makedirs(f'{DatasetPath}/images/train', exist_ok=True)
os.makedirs(f'{DatasetPath}/images/val', exist_ok=True)
os.makedirs(f'{DatasetPath}/images/test', exist_ok=True)
os.makedirs(f'{DatasetPath}/labels/train', exist_ok=True)
os.makedirs(f'{DatasetPath}/labels/val', exist_ok=True)
os.makedirs(f'{DatasetPath}/labels/test', exist_ok=True)

PathList = np.array([i.split('.')[0] for i in os.listdir(BasePath) if 'txt' in i])
random.shuffle(PathList)
TrainId = PathList[:int(len(PathList) * (1 - ValSize - TestSize))]
ValId = PathList[int(len(PathList) * (1 - ValSize - TestSize)):int(len(PathList) * (1 - TestSize))]
TestId = PathList[int(len(PathList) * (1 - TestSize)):]

for i in TrainId:
    shutil.copy(f'{BasePath}/{i}.{Postfix}', f'{DatasetPath}/images/train/{i}.{Postfix}')
    shutil.copy(f'{BasePath}/{i}.txt', f'{DatasetPath}/labels/train/{i}.txt')

for i in ValId:
    shutil.copy(f'{BasePath}/{i}.{Postfix}', f'{DatasetPath}/images/val/{i}.{Postfix}')
    shutil.copy(f'{BasePath}/{i}.txt', f'{DatasetPath}/labels/val/{i}.txt')

for i in TestId:
    shutil.copy(f'{BasePath}/{i}.{Postfix}', f'{DatasetPath}/images/test/{i}.{Postfix}')
    shutil.copy(f'{BasePath}/{i}.txt', f'{DatasetPath}/labels/test/{i}.txt')
