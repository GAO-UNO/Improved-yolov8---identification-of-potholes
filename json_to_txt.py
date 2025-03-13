import os, cv2, json
import numpy as np

Classes = ['Pothole'] # 修改成对应的类别

Base_Path = './datasets/seg_train' # 指定json和图片的位置

Path_List = [i.split('.')[0] for i in os.listdir(Base_Path)]
for path in Path_List:
    Image = cv2.imread(f'{Base_Path}/{path}.jpg')
    h, w, c = Image.shape
    with open(f'{Base_Path}/{path}.json') as f:
        Masks = json.load(f)['shapes']
    with open(f'{Base_Path}/{path}.txt', 'w+') as f:
        for idx, Mask_data in enumerate(Masks):
            Mask_label = Mask_data['label']
            if '_' in Mask_label:
                Mask_label = Mask_label.split('_')[0]
            Mask = np.array([np.array(i) for i in Mask_data['points']], dtype=np.float64)
            Mask[:, 0] /= w
            Mask[:, 1] /= h
            Mask = Mask.reshape((-1))
            if idx != 0:
                f.write('\n')
            f.write(f'{Classes.index(Mask_label)} {" ".join(list(map(lambda x:f"{x:.6f}", Mask)))}')
