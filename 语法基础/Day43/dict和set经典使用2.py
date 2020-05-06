"""
dict和set经典使用2

"""

# 7、最大值
def max_key(d):
    if len(d) == 0:
        return []
    max_key = max(d.keys())
    return (max_key, d[max_key])
print(max_key({'a': 3, 'c': 3, 'b': 2}))

# 8、最大字典值
def max_value(d):
    if len(d) == 0:
        return []
    max_val = max(d.values())
    return [(key, max_val) for key in d if d[key] == max_val]
print(max_key({'a': 3, 'c': 3, 'b': 2}))

# 9、集合最值：找出集合中的最大、最小值，并装到元组中返回
def max_min(s):
    return (max(s), min(s))
print(max_min({1, 3, 5, 7}))

# 10、单字符串：若组成字符串的所有字符仅出现一次，则被称为单字符串
def single(string):
    return len(set(string)) == len(string)
print(single('love_python'))  # False
print(single('python'))  # True
