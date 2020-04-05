"""
爬取知乎专栏关注数据

"""

import requests
import csv
import json

def crawl():
    url = "https://www.zhihu.com/api/v4/columns/c_154672552/followers"
    # 查询参数
    params = {"limit":20,
              "offset":0,
              "include":"data[*].follower_count, gender, is_followed, is-following"

    }
    #查询指定UA，否则知乎服务器会判定请求不合法
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"
    }
    response = requests.get(url, headers=headers, params=params)
    print("请求URL：", response.url)
    print("返回数据：", response.text)
    # 解析返回的数据
    csvfile = open('./res/data.csv','w',newline='')
    writer = csv.writer(csvfile, delimiter=',',quoting=csv.QUOTE_ALL)
    keys = ['id', 'name', 'url', 'gender', 'avatar_url', 'follower_count']
    writer.writerow(keys)
    i = 1
    for dic in response.json().get("data"):
        writer.writerow([dic['id'],dic['name'],dic['url'],
                        dic['gender'], dic['avatar_url'], dic['follower_count']])
        i +=1
    csvfile.close()

if __name__ == '__main__':
    crawl()