"""
分词词云

"""

# 导入词云制作库workclound和中文分词库jieba
import jieba
import wordcloud
# 构建并配置词云对象w
w = wordcloud.WordCloud(
    width=1000,
    height=700,
    background_color='#6c909e',
    colormap='GnBu',
    font_path='./res/font/SimHei.ttf')

# 调用jieba的cut()方法对原始的文本进行中文分词，得到string
txt = '孤独不曾远离，幸福却也无处不在，只是自己总是不愿意去拾起那些飘落，\
      只想把希望留给那些等待的人，他们也需要心灵的美酒……'
txtlist = jieba.lcut(txt)
string = " ".join(txtlist)

# 将string变量传入w的generate()方法，给词云输入文字
w.generate(string)

# 将词云图片导出到当前文件夹
w.to_file('./res/img/output4.png')