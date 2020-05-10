"""
抓取天气

"""

from lxml import etree
import requests

def requst_temperature():
    # 中国天气网
    url = 'http://www.weather.com.cn/weather1d/101190101.shtml#input'
    # request发起请求
    with requests.get(url) as res:
        content = res.content
        # 使用lxml的extree解析页面
        html = etree.HTML(content)
    # 通过xpath定位周边城市和景区，返回list
    location = html.xpath('//*[@id="around"]//a[@target="_blank"]/span/text()')
    # 温度list
    temperature = html.xpath('//*[@id="around"]/div/ul/li/a/i/text()')
    # 将上述两个list作业key和value合成字典
    dictionary = dict(zip(location, temperature))
    return dictionary

if __name__ == '__main__':
    print(requst_temperature())