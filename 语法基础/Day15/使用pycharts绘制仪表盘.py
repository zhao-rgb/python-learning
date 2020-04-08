"""
使用pycharts绘制仪表盘

"""
from pyecharts import charts

#仪表盘
gauge = charts.Gauge()
gauge.add('Python小例子',[('Python机器学习', 30), ('Python基础', 70.),
                        ('Python正则', 90)])
gauge.render(path="./res/仪表盘.html")
print('ok')