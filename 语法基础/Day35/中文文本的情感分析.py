"""
中文文本的情感分析

"""

from snownlp import SnowNLP

text = '一条路，人烟稀少，孤独难行。却不得不坚持前行。因为它的尽头，种着“梦想”。'
s = SnowNLP(text)
# 分词
print(s.words)
# 词性标注
tags = [x for x in s.tags]
print(tags)
# 断句
print(s.sentences)
# 拼音
print(s.pinyin)

# 情绪判断，返回值为正面情绪的概率，越接近1表示正面情绪，越接近0表示负面情绪
text1 = '这部电影真心棒'
text2 = '这部电影简直烂到爆'
s1 = SnowNLP(text1)
s2 = SnowNLP(text2)
# 这部电影真心棒，0.9959750990466912
print(text1,s1.sentiments)
# 这部电影简直烂到爆，0.0566960891729531
print(text2,s2.sentiments)

# 关键字抽取
text3 = '睡一睡，精神好，烦恼消，快乐长;睡一睡，心情好，做美梦，甜蜜蜜;睡一睡，身体健，头脑清，眼睛明。愿你酣然入梦，晚安!'
s3 = SnowNLP(text3)
print(s3.keywords(limit=5))
# 概况总结文章
print(s3.summary(limit=4))

