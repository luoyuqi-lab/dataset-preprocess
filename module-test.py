import os
import shutil
from PIL import Image

path = ("E:/sushi/")
filename = os.listdir(path)

'''img = Image.open("E:/sushi/並.gif")
img_array = img.load()
rgb_array = img_array[10, 10]
print(rgb_array)
r = rgb_array[0]
g = rgb_array[1]
b = rgb_array[2]
if r != 255:
    print('yes')
print(rgb_array)
print(r,g,b)'''

for x in range(10, 0, -1):
    print(x)