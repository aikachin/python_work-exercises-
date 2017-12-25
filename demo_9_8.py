
# test 9-8 权限
print("\n\ntest 9-8 权限------")
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
		self.privileges=Privileges()
			

class Privileges():
	def __init__(self):
		self.privileges=['can add post', 'can delete post', 'can ban post']

	def show_privileges(self):
		print("管理员的权限有：")
		for privilege in self.privileges:
			print("--" + privilege)

new_admin=Admin("jack","green",gender="male",phone="345129885")
new_admin.privileges.show_privileges()


# test 9-9 电瓶升级
print("\n\ntest 9-9 电瓶升级------")
class Car():
	def __init__(self, name, model, year):
		self.name=name
		self.model=model
		self.year=year

	def get_descriptive_name(self):
		self.car_info = "This car is " + self.name + ","
		self.car_info += self.model + ","
		self.car_info += str(self.year) + "."
		return self.car_info

class Battery():
	def __init__(self):
		self.battery_size=70
	
	def describe_battery(self):
		print("This car has a " + str(self.battery_size) + "-kWh battery.")
	
	def get_range(self):
		"""打印一条信息，说明电瓶的续航里程"""
		if self.battery_size == 70:
			range=240
		elif self.battery_size == 85:
			range=270
		
		message="This car can go approximately " + str(range)
		message+=" miles on a full charge."
		print(message)
	
	def upgrade_battery(self):
		if self.battery_size != 85:
			self.battery_size = 85


class Electric_car(Car):
	def __init__(self, name, model, year):
		super().__init__(name, model, year)
		self.battery=Battery()

my_tesla=Electric_car('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
