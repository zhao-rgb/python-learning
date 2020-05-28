"""
pandas_2
"""

import pandas as pd
# pandas之分块插入数据
# itertor取值boolean，默认为false。返回一个TextFileReader对象。以便逐块处理文件
chunk = pd.read_csv('test.csv', sep='\s+', iterator=True)
# 先读入一行，get_chunk设置为，表示一次读入一行，目标文件一共2行
print(chunk.get_chunk(1))
# 再读入下一行
# print(chunk.get_chunk(1))
# 此时已到文件末尾，再次读入会报异常

# Pandas读取之控制处理
# 假设我们的数据文件如下，date列中#值，我们想把它处理为NaN值
d = {'id': [1, 2], 'name': ['wangf', 'niit'],'age': 
     [21, 20], 'date': ['2020-05-28', '#']}
df = pd.DataFrame(d)
df.to_csv('test_date.csv', sep='', index=False)
df = pd.read_csv('test_date.csv', sep='\s+', na_values=['#'])
print('\n', df)