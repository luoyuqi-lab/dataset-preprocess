import os
import shutil
from PIL import Image

path = ("E:/sushi/")
filename = os.listdir(path)
# print(filename)
target_path = os.path.abspath("E:/sushi_white/")
target_path_y = os.path.abspath("E:/sushi_yellow/")

for file in filename:
    # print(file)
    img = Image.open("E:/sushi/" + file)
    # avoid some pic is not RGB
    img1 = img.convert('RGB')
    img_array = img1.load()
    rgb_array = img_array[0, 1]
    r = rgb_array[0]
    g = rgb_array[1]
    b = rgb_array[2]
    # print(r, g, b)
    old_path = path + file
    # print(old_path)
    # Classify white bg and non-white bg
    if r == 255 and g == 255 and b == 255:
        shutil.copy(old_path, target_path)
    else:
        shutil.copy(old_path, target_path_y)

print('copy files finished!')