"""
List基本操作
"""
# 创建
empty = []
lst = [1, 'xiaoming', 29.5, '1731266238899']
lst2 = ['001', '2019-11-11', ['三文鱼', '电烤炉']]
# 长度
print(len(lst2))   # 3
# 遍历
for _ in lst:
    print(f'{_}的类型为{type(_)}')

# 插入删除等操作
sku = lst2[2]
# append追加到list尾部
sku.append('烤鱼')
# insert到指定索引处
sku.insert(1, '牛腱子')
# pop移除尾部元素
item = sku.pop()
# remove移除、或者sku.remove(sku[0])
sku.remove('三文鱼')
print(sku)   # ['牛腱子', '电烤炉']

# 生成1到20的序列，步长为3， 放入list
a = list(range(1, 20, 3))
print(a)   # [1, 4, 7, 10, 13, 16, 19]
# 各种切片操作
print(a[-1], a[:-1], a[1:5], a[::3], a[::-3])
# 19 [1, 4, 7, 10, 13, 16] [4, 7, 10, 13] [1, 10, 19] [19, 10, 1]