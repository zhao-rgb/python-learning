"""
爬取数据

"""

import requests
import json
import pymysql
import time

def crawl():
    specials_data = []
    for offset in range(100,2000,20):
        time.sleep(1)
        url = "https://www.zhihu.com/api/v4/news_specials/list?limit=20&offset="+str(offset)+""
        print(url)
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"
        }
        response = requests.get(url,headers=headers)
        specials_data += response.json().get("data")
    return specials_data

def data_insert(specials_data):
    #打开数据库连接
    db = pymysql.connect("localhost", "root", "root", "db_python")
    # 使用cursor()方法创建一个游标对象 cursor
    cursor = db.cursor()
    val = []
    for dic in specials_data:
        item = (dic['id'], dic['updated'], dic['banner'], 
                dic['introduction'], dic['title'], dic['is_following'], dic['followers_count'])
        val.append(item)
    sql = "INSERT INTO t_special (id,updated,banner,introduction,title,is_following,followers_count) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    try:
        # 执行sql语句，批量插入
        cursor.executemany(sql,val)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    finally:
        # 关闭数据库连接
        db.close()


if __name__ == '__main__':
    list = crawl()
    print(list)
    data_insert(list)