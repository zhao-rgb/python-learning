"""
列表的定义和遍历

"""

list1 = [1,3,5,7,100]
print(list1) # [1,3,5,7,100]
list2 = ['hello'] * 3
print(list2)  # ['hello','hello','hello']
print(len(list1)) # 5
print(list1[0])   # 1
print(list1[4])   # 100
print(list1[-1])  # 100
print(list1[-3])  # 5
list1[2] = 300
print(list1) # [1,3,300,7,100]
# 通过循环下标遍历
for index in range(len(list1)):
    print(list1[index])
# 通过for循环遍历
for elem in list1:
    print(elem)
# 通过enumerate函数处理列表之后再遍历可以同时获取元素索引和值
for index, elem in enumerate(list1):
    print(index,elem)
