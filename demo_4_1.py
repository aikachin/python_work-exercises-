#!/usr/bin/python
#-*- coding:utf-8 -*-

# test 4-1
pizzas = ['水果披萨', '牛肉粒披萨', '海鲜披萨', '玛格丽特披萨']
pizzaStr = ""
for pizza in pizzas:
	print(pizza)
	print("I like " + pizza + ".")
	pizzaStr = pizzaStr + pizza + ","
print("I like a lot of kinds' pizzas, eg.: " + pizzaStr + "I really like pizza!" )

# test 4-11 你的比萨和我的比萨
friend_pizzas=pizzas[:]
pizzas.append("chicken pizza")
friend_pizzas.append("small pizza")
print("My favorite pizzas are: ")
print(pizzas)
print("My friend's favorite pizzas are: ")
print(friend_pizzas)

# test 4-12 
print("使用for循环打印出pizzas列表：")
for pizza in pizzas:
	print(pizza)
for index in range(0,len(friend_pizzas)):
	print(friend_pizzas[index])
