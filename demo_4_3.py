#!/usr/bin/python
#-*- coding:utf-8 -*-

# test 4-3 ����20
#for number in range(1,21):
#	print(number)

# test 4-4 һ����
#numbers=[]
#for number in range(1,1000001):
#	numbers.append(number)
#	print(number)

# test 4-5 ����1~1000000���ܺ�
numbers=[value for value in range(1,1000001)]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# test 4-6 ����
numbers=[]
for value in range(1,20,2):
	numbers.append(value)
	print(value)

# test 4-7 3�ı���
numbers=[]
for value in range(3,31,3):
	numbers.append(value)
	print(value)

# test 4-8 ����
numbers=[]
for value in range(1,11):
	number=value**3
	numbers.append(number)
	print(number)

# test 4-9 ��������
numbers=[ value**3 for value in range(1,11)]
for number in numbers:
	print(number)
# test 4-10 ��Ƭ
print("The first three items in the list are:")
print(numbers[:3])
print(numbers[2:5])
print(numbers[-3:])
