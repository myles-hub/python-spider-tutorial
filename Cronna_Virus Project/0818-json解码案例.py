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
