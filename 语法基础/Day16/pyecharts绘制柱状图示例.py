"""
pyecharts绘制柱状图示例

"""

from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType
# 内置主题类型可查看 pyecharts.globals.ThemeType
# 有 LIGHT DARK WHITE CHALK ESSOS INFOGRAPHIC
# MACARONS PURPLE_PASSION FOMA ROMANTIC SHINE
# VINTAGE WALDEN WESTEROS WONDERLAND 等十余种

# 第一幅图，数据固定
bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(['服饰', '箱包', '鞋帽', '电子', '数码', '户外'])
        .add_yaxis('京东', [5, 20, 36, 10, 75, 90])
        .add_yaxis('天猫', [15, 6, 45, 20, 35, 66])
        .set_global_opts(title_opts=opts.TitleOpts(title='电商销售对比'))
    )
bar.render(path='./res/电商销售对比.html')

# 第二幅图，数据分离
items = ['Java', 'C', 'Python', 'C++', 'JavaScript', 'C#', 'PHP', 'SQL']
data_list1 = [188, 166, 110, 108, 90, 80, 55, 45]
data_list2 = [190, 160, 140, 100, 80, 70, 50, 40]
bar1 = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
        .add_xaxis(items)
        .add_yaxis('2020年', data_list1)
        .add_yaxis('2019年', data_list2)
        .set_global_opts(title_opts=opts.TitleOpts(title='编程语言排行', subtitle='2019-2020'))
    )
bar1.render(path='./res/编程语言排行.html')

items = ['老班', '杨阳', '田震', '张浩杰', '颜子皓', '岳凡', '赵肖龙']
data_list1 = [2000, 920, 910, 1000, 1001, 999, 900]
data_list2 = [1500, 300, 270, 250, 300, 290, 200]
bar1 = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
        .add_xaxis(items)
        .add_yaxis('2020年', data_list1)
        .add_yaxis('2019年', data_list2)
        .set_global_opts(title_opts=opts.TitleOpts(title='云班课魅力值', subtitle='2019-2020'))
    )
bar1.render(path='./res/云班课魅力值.html')

