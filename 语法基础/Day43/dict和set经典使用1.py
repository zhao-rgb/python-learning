"""
dict和set经典使用1

"""

# 1、批量插入
d = {'a': 1, 'b': 2}
d.update({'c': 3, 'd': 4, 'e': 5})
print(d)

# 2、不存则插入，存在则不插入不更新
d = {'a': 1, 'b': 2}
x = d.setdefault('c', 3)
y = d.setdefault('a', 1)
print(d)

# 3、字典并集
def merge(d1, d2):
    return {**d1, **d2}
print(merge({'a': 1, 'b': 2},{'c': 3}))

# 4、字典差
def difference(d1, d2):
    return dict([(k, v) for k, v in d1.items() if k not in d2])
print(difference({'a': 1, 'b': 2, 'c': 3}, {'b': 2}))

# 5、按键排序
def sort_by_key(d):
    return sorted(d.items(), key=lambda x: x[0])
print(sort_by_key({'a': 3, 'b': 1, 'c': 2}))

# 6、按值排序
def sort_by_value(d):
    return sorted(d.items(), key=lambda x: x[1])
print(sort_by_value({'a': 3, 'b': 1, 'c': 2}))