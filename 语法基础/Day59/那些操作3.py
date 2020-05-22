"""
那些操作

"""

# 字符串处理成字典
s = 'k0:10|k1:2|k2:11|k3:5'
m = map(lambda x: x.split(':'), s.split('|'))
print({mi[0]: int(mi[1]) for mi in m})

# 使用filter() 求出列表中大于 10 的元素
a = [15, 2, 4, 7, 20, 344, 10, 5, -23, 204]
b = list(filter(lambda x: x > 10, a))
print(b)

# 列表内元素可重复出现，如何删除列表中的某个元素


def del_item(lst, e):
    for i in lst:
        if i == e:
            lst.remove(i)
    return lst


s = del_item([1, 2, 5, 3, 2], 3)
print(s)  # [1,5,2]
# 上述代码好像成功解除了元素3，可是下面不行
s = del_item([1, 3, 3, 3, 5], 3)
print(s)  # [1,3,5]

# 遍历的list,remove一次，移掉位置i后的所有元素索引都要减一
# 所以删除的元素重复出现在列表中，就会漏掉一个该删除的元素
# 正确做法，找到被删除元素后，删除，同时下次遍历索引不加一；未找到，遍历索引加一


def del_item2(lst, e):
    i = 0
    while i < len(lst):
        if lst[i] == e:
            lst.remove(lst[i])
        else:
            i += 1
    return lst


# 再次调用查看结果
s = del_item2([1, 3, 3, 3, 5], 3)
print(s)  # [1,5]