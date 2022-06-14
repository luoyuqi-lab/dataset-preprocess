import json

data = open("C:/Users/luoyu/OneDrive/桌面/mimi/json/hanshitie.json", 'r', encoding='UTF-8')
content = data.read()
# 把json数据放到a中
a = json.loads(content)
# 取出a中以字典形式储存的坐标
# 第一个点
print(a['shapes'][0]['points'])
# 第二个点，类推即可
print(a['shapes'][1]['points'])
# 取出第一个标签
print(a['shapes'][0]['label'])
# 取出第二个标签，其他数据同理即可
print(a['shapes'][1]['label'])