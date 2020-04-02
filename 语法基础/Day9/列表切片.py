"""
列表切片

"""

fruits = ['grape','apple','strawberry','waxberry']
fruits += ['pitaya' , 'pear' ,'mango']
# 列表切片
fruits2 = fruits[1:4]
# ['apple','strawberry','waxberry']
print(fruits2)
# 可以通过完整切片操作来复制列表
fruits3 = fruits[:]
# ['grape','apple','strawberry','waxberry','pitaya' , 'pear' ,'mango']
print(fruits3)
fruits4 = fruits[-3:-1]
print(fruits4) # ['pitaya' , 'pear']
# 可以通过反向切片操作来获取倒转后的列表的拷贝
fruits5 = fruits[::-1]
# ['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']
print(fruits5)