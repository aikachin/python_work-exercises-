"""
	import 模块
	使用方法：	模块名.函数名()
"""
#import def_describe_sandwich

"""
	from 模块 import 函数
	使用方法：	函数名()
"""
#from def_describe_sandwich import build_profile, describe_sandwiches

"""
	from 模块 import 函数 as 函数别名。
	使用方法：	函数别名()
"""
#from def_describe_sandwich import build_profile as ds

"""
	imort 模块 as 模块别名
	使用方法：	模块别名.函数名()
"""
#import def_describe_sandwich as dds

"""
	from 模块 import *
	使用方法：	函数名()
"""
from def_describe_sandwich import *



# test 8-15 打印模型
describe_sandwiches('鸡蛋\n')

user_profile=build_profile(
	'w','k',
	gender='male',
	nationality='chinese',
	age=20
	)
print(user_profile)
