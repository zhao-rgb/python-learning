"""
Pandas_3
"""
import pandas as pd
import numpy as np
# Series是pandas两个数据结构中(DataFrame Series)的一种
# 每个Series对象都是由两个数据组成
# index:它是从Numpy数组继承的Index对象，保存标签信息
# values：保存值得Numpy数组

# 1、创建一个series
# Series的标准构造函数:Series(data=None,index=None,dtype=None,name=None)
ps = pd.Series(data=[-3, 2, 1], index=['a', 'f', 'b'], dtype=np.float32)
print(ps)
print("******************")
# 2、Series增加元素(Pandas允许包含重复的标签)
ps = ps.append(pd.Series(data=[-8.0], index=['f']))
print(ps)
print("*****************")
# 3、Series访问元素，有两种方法
# 通过索引访问
print(ps[2])
# 通过标签访问
print(ps['f'])
# 4、Series之删除元素，append操作和drop操作都是发生在原数据的副本上，不是原数据上
ps = ps.drop("f")
print(ps)
print("****************")
# 5、Series之修改元素
ps['b'] = 10.0
print(ps)