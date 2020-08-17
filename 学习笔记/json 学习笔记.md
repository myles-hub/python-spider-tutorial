# JSON 模块学习

## 学习目标

- （1）应用json模块，将 **“json数据”** 转换成 **“python数据”** ，调用起来；
- （2）应用json模块，将 **“python数据”** 转换为 **“json数据”**，存储起来；



## 学习目录

- json 模块介绍
- json 转换为 python
- python 转换为 json
- 案例：解析疫情首页 json字符串数据



## 学习内容

### 1. json 模块介绍

> Json 模块是python自带的模块，其主要用于`json格式数据`与`python格式数据`间的相互转换。

<img src="C:\Users\myles\AppData\Roaming\Typora\typora-user-images\image-20200817194201850.png" alt="image-20200817194201850" style="zoom:80%;" />

### 2. json 转换为 python

#### 概念介绍

- （1）将 `JSON字符串对象` 转换为 `python数据` 类型；
- （2）将 `JSON文本对象` 转换为 `python数据` 类型；

> 一句话总结：JSON 数据转换为 python 数据，其实质就是 “将`字符串`转换为python可以方便调用的`某种数据类型`的操作” ，具体来说就是上面的2中转换实操，详细图解如下。

![image-20200817194834046](C:\Users\myles\AppData\Roaming\Typora\typora-user-images\image-20200817194834046.png)

#### 实例演示

- 类型一：json 字符串转换 python

```python
import json

# （1） json 字符串准备
json_str = '{"id":5008806,"createTime":1597662124000, "modifyTime":1597662124000, "tags":"0","countryType":2,"continents":"北美洲","provinceId":"8","provinceName":"美国"}'

# （2） 将json 字符串转换为 python字典
python_dict = json.loads(json_str)

# （3） 打印输出结果
print("(1)打印输出数据内容 >>>\n {}\n".format(python_dict))
print("(2)打印输出数据类型 >>>\n {}".format(type(python_dict)))

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
(1)打印输出数据内容 >>>
 {'id': 5008806, 'createTime': 1597662124000, 'modifyTime': 1597662124000, 'tags': '0', 'countryType': 2, 'continents': '北美洲', 'provinceId': '8', 'provinceName': '美国'}

(2)打印输出数据类型 >>>
 <class 'dict'>

Process finished with exit code 0

```



- 类型二：json文本对象转换 python 

```python
# (1) json 文本准备
demo.json数据格式，即用大括号直接包含就可以了，外围不需要任何引号；

{"id":5008806,"createTime":1597662124000, "modifyTime":1597662124000, "tags":"0","countryType":2,"continents":"北美洲","provinceId":"8","provinceName":"美国"}

# (2) 加载json文本对象，并将json文本对象转换为 python 列表
with open("/data/demo.json") as fp:
    python_list = json.load(fp)
    print("打印输出数据内容 >>> \n {}".format(python_list))
    
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
(1)打印输出数据内容 >>>
 {'id': 5008806, 'createTime': 1597662124000, 'modifyTime': 1597662124000, 'tags': '0', 'countryType': 2, 'continents': '北美洲', 'provinceId': '8', 'provinceName': '美国'}

(2)打印输出数据类型 >>>
 <class 'dict'>

Process finished with exit code 0
```







### 3. python 转换为 json

#### 概念介绍

- （1）python 类型数据转换为 **<u>json 字符串</u>**

![image-20200817212114051](C:\Users\myles\AppData\Roaming\Typora\typora-user-images\image-20200817212114051.png)

- （2）python 数据类型以**<u>json格式写入文件</u>**

![image-20200817212152977](C:\Users\myles\AppData\Roaming\Typora\typora-user-images\image-20200817212152977.png)

#### 实例演示

```python




```







### 4. 案例：解析疫情首页 json字符串数据



## 5. 命令总结

- json.loads(strings)

- json.load(fp)

- json.dumps()

- json.dump()