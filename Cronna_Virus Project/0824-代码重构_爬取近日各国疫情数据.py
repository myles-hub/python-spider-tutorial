import requests
from bs4 import BeautifulSoup
import re
import json


class CoronaVirusSpider:
    def __init__(self):
        self.home_url = "https://ncov.dxy.cn/ncovh5/view/pneumonia"

    def get_content_from_url(self, url):
        """
         1. 下载疫情首页源码
        :param url: home_url
        :return: home_page
        """
        response = requests.get(url)
        home_page = response.content.decode()
        return home_page

    def parse_home_page(self, home_page, tag_id):
        """
        解析home_page,提取script标签中的json字符，并返回python数据对象
        :param home_page: 疫情数据首页源码
        :param tag_id: 疫情数据 tag_id ="getListByCountryTypeService2true"
        :return data: 返回python数据对象
        """
        # 2. 解析疫情首页源码为文档树结构，使用标签和内容提取疫情数据
        soup = BeautifulSoup(home_page, 'lxml')
        script_tag = soup.find(id=tag_id)
        script_string = script_tag.string

        # 3. 使用正则，匹配疫情数据，提取出json字符串数据（json_str）
        json_str_list = re.findall(r"\[.+\]",script_string)
        json_str = json_str_list[0]

        # 4. 将json字符串数据转换为 python数据类型
        data = json.loads(json_str)
        return data

    def save_to_json(self, file_path, data):
        """
        将疫情python数据保存为json文件
        :param file_path: data/corona_virus.json
        :param data: 疫情数据(python字典）
        """
        with open(file_path, 'w', encoding='utf-8') as fp:
            json.dump(data, fp, ensure_ascii=False)

    def crawl_last_day_corona_virus(self):
        # 1.发送源码下载请求，并返回源码
        home_page = self.get_content_from_url(self.home_url)
        # 2. 提取引起字符串数据，并转为python对象
        data = self.parse_home_page(home_page, "getListByCountryTypeService2true")
        # 3. 保证python数据为json文件
        self.save_to_json(r"data/last_day_corona_virus.json", data)

    def run(self):
        self.crawl_last_day_corona_virus()
if __name__ == "__main__":
    spider = CoronaVirusSpider()
    spider.run()


