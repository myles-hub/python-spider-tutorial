import json

# 准备json字符串数据
json_str = '[{"a":1,"b":2,"c":3,"d":4,"e":5}]'

# 1. 将json字符串转python
python_data = json.loads(json_str)
print(python_data)
print(type(python_data))

# 准备json文件 dump.json
# 2. 将json文件转换为python

with open("dump.json") as fp:
    json_python_data = json.load(fp)
    print(json_python_data)
    print(type(json_python_data))