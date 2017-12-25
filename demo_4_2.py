#!/usr/bin/python
#-*- coding:utf-8 -*-

# test 4-2
animals = ['dog', 'cat', 'rabbit']
animalStr = ""
for animal in animals:
	print(animal)
	print("A " + animal + " would make a great pet.")
	animalStr = animalStr + animal + ", "
print((animalStr + "any of these animals would make a great pet!" ).title())
