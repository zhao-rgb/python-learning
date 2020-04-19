"""
excel操作

"""

import xlrd
import wordcloud
import random

# 1.打开工作蒲
workbook = xlrd.open_workbook('./res/excel/班级资料卡片.xlsx')

# 2.工作表
# 输出所有sheet的名字
print(workbook.sheet_names())
# 输出所有的sheet
print(workbook.sheets())
# 根据索引获取sheet
print(workbook.sheet_by_index(0))
# 根据名字获取sheet
print(workbook.sheet_by_name('t_soft'))
# 3.行、列操作
sheet1 = workbook.sheets()[0]
# 获取行数
print(sheet1.nrows)
# 获取列数
print(sheet1.ncols)
# 获取第18行的内容
print(sheet1.row_values(17))
# 获取第2列的内容
print(sheet1.col_values(1))
list = sheet1.col_values(1)+sheet1.col_values(13)
w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='#eeeeee',
                        colormap='tab20b',
                        font_path='./res/font/SimHei.ttf')
string = " ".join(list)
w.generate(string)
w.to_file('./res/img/班级资料卡词云.png')
# 4.单元格的操作
cell1 = sheet1.cell(17, 1).value
print(cell1)
cell2 = sheet1.row(17)[1].value
print(cell2)
cell3 = sheet1.cell(17, 2).value
print(cell3)
cell4 = sheet1.col(2)[17].value
print(cell4)
# 5.日期类型 （在对应的单元格准备好日期数据)
# date_value = xlrd.xldate_as_datetime(
#     sheet1.cell_value(1, 6), workbook.datemode)
# print(type(date_value), date_value)

