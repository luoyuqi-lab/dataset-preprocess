import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mping

data = np.load('C:/Users/luoyu/OneDrive/桌面/7zsbeue3kuoaj0y/coords_seg.npy')
print(data)
# format: rectangle (left, top, right, bottom)

plt.xlim((0, 150))
plt.ylim((150, 0))
plt.plot([data[0][0], data[0][2]], [data[0][1], data[0][1]], color='red')
plt.plot([data[0][2], data[0][2]], [data[0][1], data[0][3]], color='red')
plt.plot([data[0][2], data[0][0]], [data[0][3], data[0][3]], color='red')
plt.plot([data[0][0], data[0][0]], [data[0][3], data[0][1]], color='red')

plt.plot([data[1][0], data[1][2]], [data[1][1], data[1][1]], color='red')
plt.plot([data[1][2], data[1][2]], [data[1][1], data[1][3]], color='red')
plt.plot([data[1][2], data[1][0]], [data[1][3], data[1][3]], color='red')
plt.plot([data[1][0], data[1][0]], [data[1][3], data[1][1]], color='red')

plt.plot([data[2][0], data[2][2]], [data[2][1], data[2][1]], color='red')
plt.plot([data[2][2], data[2][2]], [data[2][1], data[2][3]], color='red')
plt.plot([data[2][2], data[2][0]], [data[2][3], data[2][3]], color='red')
plt.plot([data[2][0], data[2][0]], [data[2][3], data[2][1]], color='red')

plt.plot([data[3][0], data[3][2]], [data[3][1], data[3][1]], color='red')
plt.plot([data[3][2], data[3][2]], [data[3][1], data[3][3]], color='red')
plt.plot([data[3][2], data[3][0]], [data[3][3], data[3][3]], color='red')
plt.plot([data[3][0], data[3][0]], [data[3][3], data[3][1]], color='red')

plt.plot([data[4][0], data[4][2]], [data[4][1], data[4][1]], color='red')
plt.plot([data[4][2], data[4][2]], [data[4][1], data[4][3]], color='red')
plt.plot([data[4][2], data[4][0]], [data[4][3], data[4][3]], color='red')
plt.plot([data[4][0], data[4][0]], [data[4][3], data[4][1]], color='red')




pic = mping.imread('C:/Users/luoyu/OneDrive/桌面/7zsbeue3kuoaj0y/logo_resized.png')
plt.imshow(pic)

plt.show()