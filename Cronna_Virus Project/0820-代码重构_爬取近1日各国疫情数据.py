import requests
from bs4 import BeautifulSoup
import json
import re


class CoronaVirusSpider:

    def __init__(self):
        self.url = "https://ncov.dxy.cn/ncovh5/view/pneumonia"

    def get_content_from_url(self):
        """
        获取指定标签中的指定内容字符串
        :param: 请求的url
        :return: 响应内容字符串
        """
        response = requests.get(self.url)
        home_page = response.content.decode("utf-8")
        return home_page

    def parse_home_page(self, home_page):
        """
        解析网页源码，通过指定标签和字符串内容获取json字符，然后转换获取python数据
        :param: home_page 首页内容
        :return: 解析转换后的python数据
        """
        # 2. 解析网页源码为文档树结构，然后通过标签和内容其他需要的内容；
        soup = BeautifulSoup(home_page, 'lxml')
        script_tag = soup.find(id="getListByCountryTypeService2true")
        strings = script_tag.string

        # 3. 使用re模块进行字符串匹配提取json字符串（re.findall 获取到的是列表，我们要的字符串）
        json_str_list = re.findall("\[.+\]", strings)
        json_str = json_str_list[0]

        # 4. 将json字符串数据转换为 python数据对象；
        data = json.loads(json_str)
        return data

    def save_to_json(self, data, path):
        """
        5. 将python对象以json格式存储起来；
        :param:
        :return:
        """
        with open(path, 'w', encoding='utf-8') as fp:
            json.dump(data, fp, ensure_ascii=False)

    def crawl_last_day_corona_virus(self):
        """
        采集最近一天各国疫情的数据
        :return:
        """
        # 1. 发送请求，获取首页内容
        home_page = self.get_content_from_url()
        # 2. 解析首页内容，获取最近一天疫情各国数据
        last_day_corona_virus = self.parse_home_page(home_page)
        # 3. 保存疫情json数据
        self.save_to_json(last_day_corona_virus, r"./data/last_dat_corona_virus.json")

    def run(self):
        self.crawl_last_day_corona_virus()


if __name__ == "__main__":
    spider = CoronaVirusSpider()
    spider.run()