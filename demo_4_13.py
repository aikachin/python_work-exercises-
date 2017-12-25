#!usr/bin/python
#-*- coding:utf-8 -*-

# test 4-13
menu_foods=("fish","meat","chicken","duck","milk")
for food in menu_foods:
    print(food)
#menu_foods[1]="sea" 无法修改元组中的元素
menu_foods=("fish","meat","xia","yangrou","milk")
for food in menu_foods:
    print(food)
