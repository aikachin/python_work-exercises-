#!/usr/bin/python
#-*- coding:utf-8 -*-

# test 4-1
pizzas = ['ˮ������', 'ţ��������', '��������', '�����������']
pizzaStr = ""
for pizza in pizzas:
	print(pizza)
	print("I like " + pizza + ".")
	pizzaStr = pizzaStr + pizza + ","
print("I like a lot of kinds' pizzas, eg.: " + pizzaStr + "I really like pizza!" )

# test 4-11 ��ı������ҵı���
friend_pizzas=pizzas[:]
pizzas.append("chicken pizza")
friend_pizzas.append("small pizza")
print("My favorite pizzas are: ")
print(pizzas)
print("My friend's favorite pizzas are: ")
print(friend_pizzas)

# test 4-12 
print("ʹ��forѭ����ӡ��pizzas�б�")
for pizza in pizzas:
	print(pizza)
for index in range(0,len(friend_pizzas)):
	print(friend_pizzas[index])
