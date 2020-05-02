"""
字符串高频操作

"""

 # re 为正则表达式库
import re
# strip 用于去除字符串前后的空格
print(' I love python\t\n '.strip())
# replace 用于字符串的替换
print('i love python'.replace(' ', '_'))
# join 用于合并字符串
print('_'.join(['book', 'store', 'count']))
# title 用于单词的首字符大写
print('i love python'.title())
# find 用于返回匹配字符串的起始位置索引
print('i love python'.find('python'))

# 正则
# 密码安全要求：6 到 12位，包含英语字母和数字
# 方法：\da-zA-Z 满足“密码只包含英文字母和数字”
# \d 匹配数字 0-9
# a-z 匹配所有小写字符：A-Z 匹配所有大写字符
# 选用最保险的 fullmatch 方法，查看是否整个字符串都匹配
pat = re.compile(r'[\da-zA-Z]{6, 12}')
print(pat.fullmatch('qaz12'))   # 返回 None，长度小于 6
print(pat.fullmatch('qaz12wsxedc43434'))    # None 长度大于 12
print(pat.fullmatch('qaz_231'))  # None 含有下划线
print(pat.fullmatch('n0passw0Rd'))  # 符合