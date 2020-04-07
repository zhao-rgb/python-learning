"""
元组类型练习

"""

#定义元组
t = ('赵肖龙', 20, True, '江苏无锡')
print(t)
# 获取元组中的元素
print(t[0])
print(t[3])
# 遍历元组中的值
for member in t:
    print(member)
# 重新给元组赋值
# t[0] = 'zxl' # TypeError
# 变量t重新引用了新的元组原来的元组将被垃圾回收
t = ('zxl', 22, True, '江苏南京')
print(t)
# 将元组转换成列表
person = list(t)
print(person)
# 列表是可以修改它的元素的
person[0] = '陈冠希'
person[1] = 30
print(person)
# 将列表转换成元组
fruits_list = ['apple', 'banana', 'orange']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)