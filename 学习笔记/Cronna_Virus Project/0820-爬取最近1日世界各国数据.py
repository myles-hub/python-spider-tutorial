import requests
from bs4 import BeautifulSoup
import json
import re

# 1. 下载疫情首页源码
url = "https://ncov.dxy.cn/ncovh5/view/pneumonia"
response = requests.get(url)
home_page = response.content.decode("utf-8")

# 2. 解析网页源码为文档树结构，然后通过标题和内容其他需要的内容；
soup = BeautifulSoup(home_page, 'lxml')
script_tag = soup.find(id="getListByCountryTypeService2true")
strings = script_tag.string

# 3. 使用re模块进行字符串匹配提取json字符串（re.findall 获取到的是列表，我们要的字符串）
json_str_list = re.findall(r"\[.+\]", strings)
json_str = json_str_list[0]

# 4. 将json字符串数据转换为 python数据对象；
last_day_cornna_virus = json.loads(json_str)
print(type(last_day_cornna_virus))

# 5. 将python对象以json格式存储起来；
with open(r"./data/last_day_cornna_virus.json", 'w', encoding='utf-8') as fp:
    json.dump(last_day_cornna_virus, fp, ensure_ascii=False)
