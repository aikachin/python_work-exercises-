# test 9-6 冰淇淋小店
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
	
	"""累加餐馆就餐人数"""
	def increment_number_served(self, number_served_per_day):
		self.number_served+=number_served_per_day

my_restaurant=Restaurant("蓝天烧烤", "烧烤")
my_restaurant.describe_restaurant()
#my_restaurant.set_number_served(3)
my_restaurant.print_number_served()
my_restaurant.increment_number_served(5)
my_restaurant.print_number_served()


class IceCreamStand(Restaurant):
	"""初始化冰淇淋小店"""
	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		"""初始化冰淇淋小店名字"""
		self.restaurant_name="蓝天冰淇淋小店"
		self.flavors=['草莓', '芒果', '香蕉', '菠萝']
	
	def describe_menu(self):
		print("本店：" + self.restaurant_name)
		print("提供的冰淇淋口味有：")
		for flavor in self.flavors:
			print("  --" + flavor)

my_icecream=IceCreamStand("", "icecream")
my_icecream.describe_menu()


# test 9-7 管理员
print("\n\ntest 9-7 管理员------")
class User():
	"""初始化用户类"""
	def __init__(self, first_name, last_name, **user_info):
		self.first_name=first_name
		self.last_name=last_name
		self.user_name=self.first_name + " " + self.last_name
		self.user_infos=user_info
		self.login_attempts=0

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

class Admin(User):
	def __init__(self, first_name, last_name, **user_info):
		super().__init__(first_name, last_name, **user_info)
		self.privileges=['can add post', 'can delete post', 'can ban post']
	
	def show_privileges(self):
		print("管理员的权限有：")
		for privilege in self.privileges:
			print("--" + privilege)

new_admin=Admin("jack", "green", gender='male', phone='3385421578')
new_admin.describe_user()
new_admin.show_privileges()
