from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mping

img = Image.open("C:/Users/luoyu/OneDrive/桌面/cut.gif")
img1 = img.convert('RGB')
img_array = img1.load()
rgb_array = img_array[138, 68]
print(img1.mode)
print(rgb_array)
'''width, hight = img.size
for w in range(0, width):
    for h in range(0, hight):
        rgb =img_array[w, h]
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]
        if r > 40 and g > 40 and b > 40 or r > 80:
            img_array[w, h] = (255, 255, 255)

img1 = img.save("C:/Users/luoyu/OneDrive/桌面/222.jpg")

plt.subplot(2, 1, 2)
plt.imshow(img)
plt.show()
'''
