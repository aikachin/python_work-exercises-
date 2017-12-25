#!usr/bin/python
# -*- coding:utf-8 -*-
car = 'audi'
print("Is car == 'audi'? I predict True.")
print(car == 'audi')

print("\nIs car == 'Audi'? I predict False.")
print(car == 'Audi')
print("\n")

cars = ['audi','bmw','subaru','toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())
print("\n")

age = 12
if age<4:
	price=0
elif age<18:
	price=5
else:
	price=10
print("Your admission cost is $" + str(price) + ".")
