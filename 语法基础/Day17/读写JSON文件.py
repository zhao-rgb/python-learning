"""
读写JSON文件

"""

#Json模块主要有四个比较重要的函数，分别是：
#dump - 将Python对象按照JSON格式序列化到文件中
#dumps - 将Python对象处理成JSON格式的字符串
#dump - 将文件中的JSON数据反序列化成对象
#dump - 将字符串的内容反序列化成Python对象
import json

def main():
    #定义字典对象
    mydict = {
        'name':'zxl',
        'age':20,
        'qq':1019916061,
        'frends':['qj','swl'],
        'cars':[
            {'brand':'宝马','max_speed':300},
            {'brand':'AE86','max_speed':400}
        ]
    }
    try:
        #将字典对象序列化到文件
        with open('./res/zxl.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict,fs)
    except IOError as e:
        print(e)
    print('保存数据完成!')

    try:
        #从文件中读入，反序列化成对象
        with open('./res/zxl.json', 'r', encoding='utf-8') as fs:
            mydict = json.load(fs)
            print(mydict)

    except FileNotFoundError as e:
        print(e)
    except IOError as e:
        print(e)
    print('保存数据完成!')

if __name__ == '__main__':
    main()