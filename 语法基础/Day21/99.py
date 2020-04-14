"""
pyecharts绘制柱状图示例
@Date 2020.04.11
"""
import pyecharts.options as opts
from pyecharts.charts import Pie


x_data = ["我的开源项目", "内推招聘", "一图胜千言", "开发工具推荐", "读书笔记", "今天学到了", "每天一道算法题"]
y_data = [5965, 9190, 6005, 7986, 4091, 6256, 8576]
data_pair = [list(z) for z in zip(x_data, y_data)]
data_pair.sort(key=lambda x: x[1])


(
    Pie(init_opts=opts.InitOpts(width="1600px", height="800px", bg_color="#2c343c"))
    .add(
        series_name="访问来源",
        data_pair=data_pair,
        rosetype="radius",
        radius="55%",
        center=["50%", "50%"],
        label_opts=opts.LabelOpts(is_show=False, position="center"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="专题关注人数对比图",
            pos_left="center",
            pos_top="20",
            title_textstyle_opts=opts.TextStyleOpts(color="#fff"),
        ),
        legend_opts=opts.LegendOpts(is_show=False),
    )
    .set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        ),
        label_opts=opts.LabelOpts(color="rgba(255, 255, 255, 0.3)"),
    )
    .render("./res/掘金数据饼状图.html")
)