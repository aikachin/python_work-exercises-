#!/usr/bin/python
#-*- coding:utf-8 -*-

# test 3-10
things = ['river_changjiang', 'river_huanghe', 'country_china', 'country_egypt', 
	'city_tokyo', 'city_shanghai']
print('things contains : ')
print(things)
things.append('bird')
print('\nnow things contains : ')
print(things)
print(', and length is : ' + str(len(things)))
print("remove掉bird")
things.remove('bird')
print("当前things列表内容为：")
print(things)
things.reverse()
print("第一次reverse()后，things列表内容为：")
print(things)
things.reverse()
print("第二次reverse()后，things列表内容为：")
print(things)
things.insert(1, 'city_悉尼')
print("插入一个元素后，当前things列表内容为：")
print(things)
print("things正向排序为：")
#things.sort()
print(sorted(things))
print("things逆向排序为：")
print(sorted(things, reverse=True))
print(things)
things.sort()
print("things正序排序，改变后为：")
print(things)
things.sort(reverse=True)
print("things倒序排序，改变后为：")
print(things)
print("things的最后1个元素为：")
print(things[-1])
print("things的倒数第3个元素为：")
print(things[-3])
ele=things.pop()
print("things的倒数第1个元素为：")
print(ele)
print("things pop()掉最后一个元素后为：")
print(things)
del things[-2]
print("things del掉倒数第2个元素后len为：")
print(len(things))
ele2=things.pop(-1)
print("things pop(-1)掉后为：")
print(things)
ele3=things[2]
things.remove(ele3)
print("things remove()掉第3个元素后为：")
print(things)
