from PIL import Image
import os
import matplotlib.pyplot as plt
# path = ("E:/sushi_white/")
# filename = os.listdir(path)
# img = Image.open(path + file)
# 确定是否所有图片都是350*350
'''n = 0
for file in filename:
    img = Image.open(path + file)
    if img.size[0] != 350 or img.size[1] != 350:
        n += 1
print(n)'''

# 把'字典网'水印裁掉
'''for file in filename:
    img = Image.open(path + file)
    cropped = img.crop((0, 0, 350, 312))
    cropped.save("E:/cropped/" + file)

print('Finish!')'''
img = Image.open("C:/Users/luoyu/OneDrive/桌面/cut.gif")
img1 = img.convert('RGB')
img_array = img1.load()
width, height = img1.size
for w in range(0, width):
    exit_flag = False
    for h in range(0, height):
        rgb = img_array[w, h]
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]
        if r < 180 and g < 180 and b < 180:
            a = w
            c = h
            exit_flag = True
            break
    if exit_flag:
        break
            # print(r, g, b)


print(a, c)
for h1 in range(0, height - 1):
    exit_flag = False
    for w1 in range(0, width - 1):
        rgb = img_array[w1, h1]
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]
        if r < 180 and g < 180 and b < 180:
            a1 = w1
            b1 = h1
            exit_flag = True
            break
    if exit_flag:
        break

for w2 in range(width - 1, 0, -1):
    exit_flag = False
    for h2 in range(0, height - 1):
        rgb = img_array[w2, h2]
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]
        if r < 180 and g < 180 and b < 180:
            a2 = w2
            b2 = h2
            exit_flag = True
            break
    if exit_flag:
        break

for h3 in range(height - 1, 0, -1):
    exit_flag = False
    for w3 in range(0, width - 1):
        rgb = img_array[w3, h3]
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]
        if r < 180 and g < 180 and b < 180:
            a3 = w3
            b3 = h3
            exit_flag = True
            break
    if exit_flag:
        break

print(a, c, a1, b1, a2, b2, a3, b3)

'''img_c = Image.new('RGB', (2, 1), (156,156,156))
plt.imshow(img_c)
print(a, b)
print(img_array[a, b])
plt.show()'''