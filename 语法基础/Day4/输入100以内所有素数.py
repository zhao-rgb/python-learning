"""
输入100以内所有素数

"""

i = 2
print('100以内的素数：')
for num in range(2,100):
    for i in range(2, num):
        if num % i == 0:
            break
        else:
            i = i + 1
    if i >= num:
        print(num, '', end='')
print()