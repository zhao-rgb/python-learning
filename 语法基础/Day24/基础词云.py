"""
基础词云

"""

import wordcloud
import random

# 创建词云对象
w = wordcloud.WordCloud()
# 通过字符串生成词云
w.generate('A person, be good to yourself; Two person, treat each other.')
# 生成本地图片
w.to_file('./res/img/output1.png')


# 创建词云对象，设置词云图片宽、高、字体、背景颜色等参数
# 中文字体需要提前下载中文字体文件
w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='#eeeeee',
                        font_path='./res/font/SimHei.ttf')
w.generate('世界太小，我曾试着想打开生活的链节，让更多的人走进这个世界，\
    可是自私的心多少次悄悄的告诉自己那是傻瓜的心理，怎能把你忘记，也至于一次次的把心弄丢了，\
    左右寻觅不见时，不经意间却发现原来在你那里 ……')
w.to_file('./res/img/output2.png')