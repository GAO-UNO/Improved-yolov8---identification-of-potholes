from ultralytics import YOLO
import os
# 加载模型
model = YOLO(".\\runs\segment\\train_best\weights\\best.pt")
path = '.\datasets\\testdata\\testdata_V2'
files = os.listdir(path)

for file in files:
    file_name = '.\datasets\\testdata\\testdata_V2\\' + file

    results = model(file_name, save=True, save_crop=True, save_txt=True)  # 对图像进行预测

