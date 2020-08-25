import requests
from bs4 import BeautifulSoup
import re
import json
from tqdm import tqdm


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

    def crawl_corona_virus(self):
        # （1）加载json文件为python可操控对象；
        with open(r'data/last_day_corona_virus.json', 'r', encoding='utf-8') as fp:
            last_day_corona_virus = json.load(fp)

        # （2）通过关键字提取url链接；
        for country in tqdm(last_day_corona_virus, "采集1月23日后的每日疫情数据"):
            country_url = country["statisticsData"]
            # print(country_url)

            # （3）通过链接逐个现在各个1月23日以来每日疫情json数据
            country_json_str = self.get_content_from_url(country_url)

            # （4）转换json数据为python可操作对象,并提取所需要疫情数据；
            country_dict = json.loads(country_json_str)
            data_of_country_dict = country_dict['data']
            # print(data_of_country_dict)

            # （5）添加“国家”关键字信息到每日数据记录中，以方便后续识别和调用；
            for everyday in data_of_country_dict:
                everyday["provinceName"] = country["provinceName"]
                everyday["countryShortCode"] = country["countryShortCode"]

        # （6）最后，在将python数据保证为json文件存储起来；
        self.save_to_json('data/corona_virus.json')

    def run(self):
        # self.crawl_last_day_corona_virus()
        # self.crawl_corona_virus()

if __name__ == "__main__":
    spider = CoronaVirusSpider()
    spider.run()


