# test 9-13 OrderedDict
from collections import OrderedDict

python_dict=OrderedDict()
python_dict['circle']='A structure of codes that keep your program excuting the following actions until the expected condition come up.'
python_dict['boolean_expression']='一段返回True或者False的代码表达式。'
python_dict['range(x,y)']='表示一组在 x ~ y-1 之间的连续整数的列表.'
python_dict['list']='Python中能够存储多个数据的一种结构的名称.'
python_dict['元组']='Python中列表的一种，用来存储一组不需要改变（也无法修改）的数据的结构，但是可以重复定义（赋值）.'

for key,value in python_dict.items():
	print(key + "：" + value)


# test 9-14 骰子
from random import randint
class Die():
	def __init__(self, side=6):
		self.side=side
	
	def roll_die(self):
		x=randint(1, self.side)
		print(x)


six_die=Die()
#print("下面开始掷骰子，次数为：")
count=int(input("请输入掷6面骰子次数："))
while count > 0:
	six_die.roll_die()
	count-=1

ten_die=Die(10)
count=int(input("请输入掷10面骰子次数："))
while count > 0:
	ten_die.roll_die()
	count-=1

twenty_die=Die(20)
count=int(input("请输入掷20面骰子次数："))
while count > 0:
	twenty_die.roll_die()
	count-=1
