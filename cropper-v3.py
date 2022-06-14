from PIL import Image
import os
import matplotlib.pyplot as plt
# For white bg, single characters, full cropper.
path = ("E:/cropped/")
filename = os.listdir(path)
for file in filename:
    img = Image.open(path + file)
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
    cropped = img1.crop((a, b1, a2, b3))
    cropped.save("E:/cropped-finish/" + file)