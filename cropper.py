from PIL import Image

img = Image.open("C:/Users/luoyu/OneDrive/桌面/暗.jpg")
print(img.size)
'''cropped = img.crop((0,0,350,300))
cropped.save("C:/Users/luoyu/OneDrive/桌面/boyuantie-1.jpg")
img2 = Image.open("C:/Users/luoyu/OneDrive/桌面/boyuantie-1.jpg")
print(img2.mode)
img3 =img2.convert('RGBA')'''
print(img.mode)
img1 = img.convert('RGBA')
newImage = []
for item in img1.getdata():
    if item[:3] != (44, 44, 44):
        newImage.append((255, 255, 255, 0))
    else:
        newImage.append(item)

img.putdata(newImage)
img.save('C:/Users/luoyu/OneDrive/桌面/boyuantie-nobg.gif')
'''img_array = img.load()
rgb_array = img_array[36, 303]
print(rgb_array)'''
