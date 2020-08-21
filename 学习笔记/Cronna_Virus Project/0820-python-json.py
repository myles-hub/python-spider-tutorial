import requests
from bs4 import BeautifulSoup
import re
import json

# 1. 下载疫情首页源码
url = "https://ncov.dxy.cn/ncovh5/view/pneumonia"
response = requests.get(url)
home_page = response.content.decode()

# 2. 解析疫情首页源码为文档树结构，使用标签和内容提取疫情数据
soup = BeautifulSoup(home_page, 'lxml')
script_tag = soup.find(id="getListByCountryTypeService2true")
strings = script_tag.string

# 3. 使用正则，匹配疫情字符串数据（json_str）
json_str_list = re.findall(r"\[.+\]",strings)
json_str = json_str_list[0]

# 4. 将json字符串数据转换为 python数据类型
last_day_cornna_virus = json.loads(json_str)
print(last_day_cornna_virus)