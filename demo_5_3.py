#!usr/bin/python
# -*- coding:utf-8 -*-

# test 5-3
alien_color = 'green'
if alien_color == 'green':
	print("Player A has got 5 points.")
elif alien_color == 'yellow':
	print("Player A has got 10 points.")
elif alien_color == 'red':
	print("Player A has got 15 points.")

# test 5-6
age = 32
if age<2:
	print("He is a child.")
elif age<4:
	print("他正蹒跚学步.")
elif age<13:
	print("他说儿童.")
elif age<20:
	print("她是青少年.")
elif age<65:
	print("He is an adult.")
elif age>=65:
	print("He is an old man.")

# test 5-7
favorite_fruits=['apple','pear','peach']
if 'apple' in favorite_fruits:
	print("I like apples")
if 'pear' in favorite_fruits:
	print("I like pears")
if 'peach' in favorite_fruits:
	print("I like peaches")
if 'banana' in favorite_fruits:
	print("I like bananas")
if 'strawberries' in favorite_fruits:
	print("I like strawberries")
