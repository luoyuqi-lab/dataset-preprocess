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


data = open("C:/Users/luoyu/OneDrive/桌面/mimi/json/hanshitie.json", 'r', encoding='UTF-8')

content = data.read()
a = json.loads(content)
print(a['shapes'][0]['points'])
print(a['shapes'][0]['points'][0][0])
print(dict.keys(a))
plt.figure(dpi=500)
pic = mping.imread('C:/Users/luoyu/OneDrive/桌面/mimi/artwork/hanshitie.jpg')
plt.imshow(pic)
img = Image.open('C:/Users/luoyu/OneDrive/桌面/4.jpg')
x, y = img.size
'''plt.xlim((0, x))
plt.ylim((y, 0))
plt.Rectangle((a['shapes'][0]['points'][0][0], a['shapes'][0]['points'][0][1]),
              a['shapes'][0]['points'][1][0] - a['shapes'][0]['points'][0][0],
              a['shapes'][0]['points'][1][1] - a['shapes'][0]['points'][0][1],
              edgecolor='red', linewidth=10, fill=False)'''


ax = plt.gca()
rect0 = patches.Rectangle((a['shapes'][0]['points'][0][0], a['shapes'][0]['points'][0][1]),
              a['shapes'][0]['points'][1][0] - a['shapes'][0]['points'][0][0],
              a['shapes'][0]['points'][1][1] - a['shapes'][0]['points'][0][1],
              edgecolor='red', linewidth=0.3, fill=False)
rect1 = patches.Rectangle((a['shapes'][1]['points'][0][0], a['shapes'][1]['points'][0][1]),
              a['shapes'][1]['points'][1][0] - a['shapes'][1]['points'][0][0],
              a['shapes'][1]['points'][1][1] - a['shapes'][1]['points'][0][1],
              edgecolor='red', linewidth=0.3, fill=False)
rect2 = patches.Rectangle((a['shapes'][2]['points'][0][0], a['shapes'][2]['points'][0][1]),
              a['shapes'][2]['points'][1][0] - a['shapes'][2]['points'][0][0],
              a['shapes'][2]['points'][1][1] - a['shapes'][2]['points'][0][1],
              edgecolor='red', linewidth=0.3, fill=False)

ax.add_patch(rect0)
ax.add_patch(rect1)
ax.add_patch(rect2)
'''plt.Rectangle((3010, 96), 48, 75, edgecolor='red', linewidth=10)'''
print([a['shapes'][0]['points'][0][0], a['shapes'][0]['points'][0][1], a['shapes'][0]['points'][1][0], a['shapes'][0]['points'][1][1]], )
plt.show()
print(a['shapes'][0]['label'][0])
print(a)