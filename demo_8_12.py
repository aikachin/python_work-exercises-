# test 8-12 三明治
def describe_sandwiches(*info_list):
	print("\n顾客点的三明治包含以下辅料：")
	for info in info_list:
		print("-" + info.title())

describe_sandwiches('鸡蛋')
describe_sandwiches('鸡蛋','培根')
describe_sandwiches('鸡蛋','培根','烟熏火腿')

# test 8-13 用户简介
print("\n\ntest 8-13 用户简介")
def build_profile(first_name,last_name,**user_info):
	profile={}
	profile['first_name']=first_name
	profile['last_name']=last_name
	for key,value in user_info.items():
		profile[key]=value;
	return profile

user_profile=build_profile(
	'w','k',
	gender='male',
	nationality='chinese',
	age=20
	)
print(user_profile)

# test 8-14 汽车
print("\n\ntest 8-14 汽车")
def make_car(brand,style,**car_info):
	car_infos={}
	car_infos['brand']=brand
	car_infos['style']=style
	for key,value in car_info.items():
		car_infos[key]=value
	return car_infos

car=make_car('subaru','outback',color='blue',tow_package=True)
print(car)
