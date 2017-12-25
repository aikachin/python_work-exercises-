# test 9-4 就餐人数
class Restaurant():
	"""
	初始化定义餐馆名称、食物烹饪类型
	"""
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type
		self.number_served=0
	
	"""描述餐馆"""
	def describe_restaurant(self):
		print("Restaurant name is: " + self.restaurant_name + ".")
		print("And cuisine type is: " + self.cuisine_type + ".")
	
	"""打印餐馆开张状态"""
	def open_restaurant(self):
		print("The restaurant is opening now.")
	
	"""打印餐馆服务过的客人数"""
	def print_number_served(self):
		print("在此餐厅就餐过的人数为: " + str(self.number_served))
	
	"""初始化服务过的客人数"""
	def set_number_served(self, number_served):
		self.number_served=number_served
	
	def increment_number_served(self, number_served_per_day):
		self.number_served+=number_served_per_day

my_restaurant=Restaurant("蓝天碳烤", "碳烤")
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant2=Restaurant("蓝天小烤", "火烤")
my_restaurant2.describe_restaurant()

my_restaurant3=Restaurant("蓝天烧烤", "烧烤")
my_restaurant3.describe_restaurant()
my_restaurant3.set_number_served(3)
my_restaurant3.print_number_served()
my_restaurant3.increment_number_served(5)
my_restaurant3.print_number_served()


# test 9-5 尝试登录次数
print("\n\ntest 9-5 尝试登录次数------")
class User():
	"""初始化用户类"""
	def __init__(self, first_name, last_name, **user_info):
		self.first_name=first_name
		self.last_name=last_name
		self.user_name=self.first_name + " " + self.last_name
		self.user_infos=user_info
		self.login_attempts=0
		
		#self.user_infos={}
		#for key,value in user_info.items():
		#	self.user_infos[key]=value
	
	def describe_user(self):
		"""打印用户信息"""
		print("\nUser's infomation is below...")
		print("--First name: " + self.first_name.title())
		print("--Last name: " + self.last_name.title())
		for key, value in self.user_infos.items():
			if key != 'age':
				print("--" + key + ": " + value)
			else:
				print("--age: " + str(value))

	"""问候用户"""
	def greet_user(self):
		print("\nHello " + self.user_name.title() + ",welcome!")
	
	"""累积登录册数"""
	def increment_login_attempts(self):
		self.login_attempts+=1
	
	"""重置登录次数"""
	def reset_login_attempts(self):
		self.login_attempts=0

user1=User("jack","green",gender='male',age=34)
count=0
while count < 5:
	user1.increment_login_attempts()
	count+=1
	print(user1.login_attempts)

user1.reset_login_attempts()
print(user1.login_attempts)
