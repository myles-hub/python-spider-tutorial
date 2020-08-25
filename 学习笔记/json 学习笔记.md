# JSON 模块学习

## 学习目标

- （1）**解码**：应用json模块，将 **“json数据”** 转换成 **“python 对象”** ，调用起来；
- （2）**编码**：应用json模块，将 **“python对象”** 转换为 **“json数据”**，存储起来或传输；



## 学习目录

- json 模块介绍
- 解码：json 转换为 **python对象**
- 解码：**python对象** 转换为 json
- 案例：解析疫情首页 json字符串数据



## 学习内容

### 1. json 模块介绍

> Json 模块是python自带的模块，其主要用于`json数据`与`python数据`间的相互转换。

<img src=".\images\image-20200817194201850.png" alt="image-20200817194201850" style="zoom:80%;" />

### 2. json 转换为 python

#### 概念介绍

- （1）将 `JSON字符串对象` 转换为 `python数据` 类型；
- （2）将 `JSON文本对象` 转换为 `python数据` 类型；

> 一句话总结：JSON 数据转换为 python 数据，其实质就是 “将`字符串`转换为python可以方便调用的`某种数据类型`的操作” ，具体来说就是上面的2中转换实操，详细图解如下。

<img src=".\images\image-20200817194834046.png" alt="image-20200817194834046" style="zoom:80%;" />

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

- （1）将 `python 类型数据`转换为 **<u>json 字符串</u>**

<img src=".\images\image-20200817212114051.png" alt="image-20200817212114051" style="zoom:80%;" />

- （2）将 `python 数据类型`以**<u>json格式写入文件</u>**

<img src=".\images\image-20200817212152977.png" alt="image-20200817212152977" style="zoom:80%;" />

#### 实例演示

```python
# 准备python数据
python_data = { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } 

# python 数据转为 json数据 (获取json字符串)
json_str = json.dumps(python_data)
print(json_str)

# 将python数据转为json文件存储起来（获取json文件）
with open("dump.json", "r") as fp:
    json.dump(python_data, fp) 



```

### 4. 案例：解析疫情首页 json字符串数据

```python
import requests
from bs4 import BeautifulSoup
import re
import json

# 1. 请求疫情首页源码
url = "https://ncov.dxy.cn/ncovh5/view/pneumonia"
response = requests.get(url)
home_page = response.content.decode("utf-8")

# 2. 使用lxml 解析html文档树，获取一个soup对象，并提取疫情数据标签script
soup = BeautifulSoup(home_page, 'lxml')
script_tag = soup.find(id="getListByCountryTypeService2true")
text = script_tag.string

# 3. 使用re提取疫情json字符串
# print(text)
json_str = re.findall(r'\[.+\]', text)[0]

# 4. 解码json字符串为python数据
# print(json_str)
last_day_cornna_virus = json.loads(json_str)
print(last_day_cornna_virus)
```



### 5. 命令总结

- **解码：json -> python**
  - json.loads(strings)

  - json.load(fp)
- **编码：python -> json**
  - json.dumps(obj)
  - json.dump(obj, fp)

<img src="images\image-20200818162241246.png" alt="image-20200818162241246" style="zoom:80%;" />

### 6. 概念总结

json 是一种轻量级的数据存储格式，我们python想要去使用它，就存在一下2中场景：

> 解码过程：python想要调用json数据时，就必须对其进行解码后才能调用（解码是为了获取可以可操作的数据对象）；
> 编码过程：同样我们python中调的数据如果需要以json格式进行存储，则就需要遵循json的编码要求进行编码存储后，其才能被正常调用（编码是为了将python数据对象转换为可存储下来或传输的对象）；



- 记忆辅助
  - （1）json.load() /json.loads()  解码：其加载的目标只有一个，就是为获取一个可操作`python数据对象（obj)`；
  - （2）json.dump()/json.dumps()编码：其载入的对象只能是`python数据对象`，然后分别获取到一个`json file对象`和`json string对象`；
  - 总结：json模块的这4个关键函数方法，都是围绕着 **”python对象“** 来进行操作的，一个为了获取 **”python对象“** ,一个是为了将  **”python对象“**  转换为`文件对象`或`字符串对象`。