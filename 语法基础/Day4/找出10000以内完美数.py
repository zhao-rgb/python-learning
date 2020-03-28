"""
找出10000以内完美数

"""

for num in range(2,100001):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if num == sum:
        print(num)
print()