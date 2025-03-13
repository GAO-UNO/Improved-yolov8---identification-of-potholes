from ultralytics import YOLO
# 加载模型
model = YOLO("yolov8n-seg.pt")  # 加载预训练模型（建议用于训练）
# 训练模型
model.train(data="Datasets.yaml", epochs=100, nms=True, iou=0.7, visualize=True, cos_lr=True, amp=True, dnn=True,  lr0=0.0001, device='cpu')
