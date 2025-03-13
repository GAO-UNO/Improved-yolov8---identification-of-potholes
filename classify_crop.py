"""
该代码的作用是，根据crop结果的命名规则，判断哪些预测框是源自同一张原图
运行前需要将predict_Q1放在该代码的同一目录下
"""
import os
import shutil

# 读取每个图片识别的苹果个数
# 指定文件夹路径
folder_path = '.\predict_Q1\labels'
# 存储每个图片的苹果个数
length_crop = []
for i in range(1, 201):
    file_name = 'resized_' + str(i) + '.txt'
    # 合并文件夹和文件名路径
    file_path = os.path.join(folder_path, file_name)
    if os.path.exists(file_path):
        # 文件存在
        with open(file_path, 'r', encoding='utf-8') as file:
            # 读取文件所有行
            lines = file.readlines()
            # 输出行数
            length_crop.append(len(lines))
    else:
        # 文件不存在
        length_crop.append(0)

# 存储已经存在的序号
read_ed = []
# 存储每个图像的苹果分割的命名
crop_name = []
for i in range(1, 201):
    crop = []
    for j in range(1, length_crop[i - 1] + 1):
        flag = 0
        if j == 1:
            if i not in read_ed:
                crop.append(i)
                read_ed.append(i)
                flag = 1
        else:
            if int(str(i)+str(j)) not in read_ed:
                crop.append(int(str(i)+str(j)))
                read_ed.append(int(str(i)+str(j)))
                flag = 1
        if flag == 0:
            if j == 1:
                j += 1
            while int(str(i)+str(j)) in read_ed:
                j += 1
            crop.append(int(str(i) + str(j)))
            read_ed.append(int(str(i) + str(j)))
    crop_name.append(crop)

for i in range(0, 200):
    folder_name = '.\predict_Q1\classify_crops\\' + str(i + 1)
    # 创建文件夹
    try:
        os.mkdir(folder_name)
    except FileExistsError:
        # 文件夹已存在
        pass
    for name in crop_name[i]:
        # 源文件路径
        source_file = os.path.join('.\\predict_Q1\crops\Apple', 'resized_' + str(name) + '.jpg')

        # 目标文件夹路径
        destination_folder = folder_name

        # 复制文件
        try:
            shutil.copy(source_file, destination_folder)
        except FileNotFoundError:
            print("源文件不存在")
        except FileExistsError:
            # 目标文件已存在
            pass


