# import json
#
# # python 数据准备
# python_dict = [{'a':1, 'b':2, 'c':3, 'd':4, 'e':5}]
#
# # 将 python 数据类型转为 json 字符串
# json_str = json.dumps(python_dict)
# print(json_str)
# print(type(json_str))
#
# # 将 python 类型数据转为 json文件存储起来；
# with open("dump.json", 'w') as fp:
#     json.dump(python_dict, fp)


import json
# 准备python数据
python_data = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5}

# python 数据转为 json数据 (获取json字符串)
json_str = json.dumps(python_data)
print(json_str)

# 将python数据转为json文件存储起来（获取json文件）
with open("dump.json", "w") as fp:
    json.dump(python_data, fp)