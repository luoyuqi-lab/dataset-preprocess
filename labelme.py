import labelme
import os
import json
from labelme import labelme_draw_json

f = open("C:/Users/luoyu/OneDrive/桌面/114514.json")
data = labelme_draw_json("C:/Users/luoyu/OneDrive/桌面/114514.json")
print(data)
