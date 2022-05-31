from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mping

img = Image.open("C:/Users/luoyu/OneDrive/桌面/7.jpg")
plt.figure(figsize=(10,10), dpi=150)
plt.subplot(3, 1, 1)
plt.imshow(img)
# img1 = img.convert('RGBA')
img_array = img.load()
rgb_array = img_array[1, 1]
print(img.mode)
print(rgb_array)
img_c = Image.new('RGB', (2, 1), rgb_array)
plt.subplot(3, 1, 3)
plt.imshow(img_c)
width, hight = img.size
for w in range(0, width):
    for h in range(0, hight):
        rgb =img_array[w, h]
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]
        if r > 65 and g > 65 and b > 65 or r > 90:
            img_array[w, h] = (255, 255, 255)

img1 = img.save("C:/Users/luoyu/OneDrive/桌面/777.jpg", quality=95)

plt.subplot(3, 1, 2)
plt.imshow(img)
plt.show()
'''plt.subplot(1, 2, 2)
plt.imshow(img1)
plt.show()'''
