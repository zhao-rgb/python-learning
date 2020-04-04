"""
requests请求api，用字典和列表保存为json

"""

import json
import requests
resp = requests.get(
    'http://api.tianapi.com/allnews/index?key=a2fba4cc608bcd3beb08629562bc9e15&num=10&col=7'
)
newslist = json.loads(resp.text)['newslist']
result = []
data = './res/data.json'
for news in newslist:
    temp_dict = {}
    temp_dict['title'] = news['title']
    temp_dict['pic_url'] = news['picUrl']
    result.append(temp_dict)
with open(data, 'w') as f:
    json.dump(result, f)
