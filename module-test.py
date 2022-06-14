from PIL import Image
import os
import matplotlib.pyplot as plt
import matplotlib.image as mping
import matplotlib.patches as patches
import json
# For yellow bg, single characters, full cropper.

'''img = Image.open("E:/sushi_yellow/安.gif")
img1 = img.convert('RGB')
img_array = img1.load()
rgb_array = img_array[106, 242]'''


data = open("C:/Users/luoyu/OneDrive/桌面/1-IV-D1-01.json", 'r', encoding='UTF-8')

content = data.read()
a = json.loads(content)
print(a['shapes'][0]['points'])