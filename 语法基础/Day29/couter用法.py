"""
couter用法

"""
from collections import Counter


words = [
    'look', 'into', 'head', 'my', 'head', 'around', 'the', 'eyes', 
    'under', 'under', 'eyes', 'head', 'eyes', 'pick', 'not', 
    'eyes', 'futher', 'not','look', 'the', 'my', 'eyes', 'left', 
    'behind', 'into', 'mouse', 'the',  'shoulder', 'eyes', 'the', 'right', 'head'
]

counter = Counter(words)
# 找出序列中出现次数最多的元素
print(counter.most_common(3))

c = Counter(a=4, b=2, c=0, d=-2)
# elements()按照counter的计数，重复返回的元素
list = list(c.elements())
print(list)