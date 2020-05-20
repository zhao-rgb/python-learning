"""
Counter: 分析数据的时候统计计数
@Date 2020.05.19
"""
from collections import Counter
# 习惯使用list的，往往会这样统计
sku_purchase = [3, 8, 3, 10, 3, 3, 1, 3, 7, 6, 1, 2, 7, 0, 7, 9, 1, 5, 1, 0]

d = {}
for i in sku_purchase:
    if d.get(i) is None:
        d[i] = 1
    else:
        d[i] += 1

d_most = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
# 最受欢迎的商品（键为商品编号），排序结果
print(d_most)
# 如果使用Counter，能写出更加简化的代码
# 一行代码搞定，使输出统计结果，并且输出按照采购次数的有大到小排序好的列表
print(Counter(sku_purchase).most_common)
# 除此之外，使用Counter还能快速统计一句话中单词出现的次数，一个单词中字符出现次数
print(Counter('I love python so much').most_common())