import requests
from bs4 import BeautifulSoup
import json
import re
from tqdm import tqdm

class CoronaVirusSpider:

    def __init__(self):
        self.home_url = "https://ncov.dxy.cn/ncovh5/view/pneumonia"

    def get_content_from_url(self, url):
        """
        获取指定标签中的指定内容字符串
        :param: 请求的url
        :return: 响应内容字符串
        """
        response = requests.get(url)
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
        home_page = self.get_content_from_url(self.home_url)
        # 2. 解析首页内容，获取最近一天疫情各国数据
        last_day_corona_virus = self.parse_home_page(home_page)
        # 3. 保存疫情json数据
        self.save_to_json(last_day_corona_virus, r"./data/last_dat_corona_virus.json")

    def crawl_corona_virus(self):
        # 1. 加载json文档数据，将其转换为python可操作数据对象（字典）
        with open(r"data/last_day_corona_virus.json",'r', encoding='utf-8') as fp:
            last_day_corona_virus = json.load(fp)
            # print(last_day_corona_virus)

        # 定义一个列表用于存放1月23以来的每日疫情数据
        corona_virus = []
        # 2. 通过关键字，从疫情数据字典中提取1月23日后的每日疫情的url链接
        for day_data in tqdm(last_day_corona_virus, "采集1月23日以来各国的每日疫情数据"):
            country_day_data_url = day_data['statisticsData']
            # print(country_day_data_url)

            # 3. 直接通过url获取源码内容（json_str）；
            country_day_data_content = self.get_content_from_url(country_day_data_url)
            # print(country_day_data_content)

            # 4. 将json字符串数据转换为python字典，以方便添加“国家”相关信息
            country_day_data_dict = json.loads(country_day_data_content)
            country_day_data_statistics = country_day_data_dict['data']
            # print(country_day_data_statistics)

            # 5. 给每日统计数据添加“国家”关键字信息
            for one_day in country_day_data_statistics:
                one_day["provinceName"] = day_data["provinceName"]
                one_day["countryShortCode"] = day_data["countryShortCode"]
            # print(country_day_data_statistics)
            corona_virus.extend(country_day_data_statistics)

        # 6. 最后将python数据存储为json文档(调用self.save())；
        self.save_to_json(corona_virus, r'data/corona_virus.json')

    def run(self):
        # self.crawl_last_day_corona_virus()
        self.crawl_corona_virus()


if __name__ == "__main__":
    spider = CoronaVirusSpider()
    spider.run()
