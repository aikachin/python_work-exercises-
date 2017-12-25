#!/usr/bin/python
#-*- coding:utf-8 -*-

# test 4-3 数到20
#for number in range(1,21):
#	print(number)

# test 4-4 一百万
#numbers=[]
#for number in range(1,1000001):
#	numbers.append(number)
#	print(number)

# test 4-5 计算1~1000000的总和
numbers=[value for value in range(1,1000001)]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# test 4-6 奇数
numbers=[]
for value in range(1,20,2):
	numbers.append(value)
	print(value)

# test 4-7 3的倍数
numbers=[]
for value in range(3,31,3):
	numbers.append(value)
	print(value)

# test 4-8 立方
numbers=[]
for value in range(1,11):
	number=value**3
	numbers.append(number)
	print(number)

# test 4-9 立方解析
numbers=[ value**3 for value in range(1,11)]
for number in numbers:
	print(number)
# test 4-10 切片
print("The first three items in the list are:")
print(numbers[:3])
print(numbers[2:5])
print(numbers[-3:])
