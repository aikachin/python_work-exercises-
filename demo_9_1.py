# test 9-1 餐馆
class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type
	
	def describe_restaurant(self):
		print("Restaurant name is: " + self.restaurant_name + ".")
		print("And cuisine type is: " + self.cuisine_type + ".")
	
	def open_restaurant(self):
		print("The restaurant is opening now.")

my_restaurant=Restaurant("蓝天碳烤", "碳烤")
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant2=Restaurant("蓝天小烤", "火烤")
my_restaurant2.describe_restaurant()

my_restaurant3=Restaurant("蓝天烧烤", "烧烤")
my_restaurant3.describe_restaurant()


# test 9-3 用户
print("\n\ntest 9-3 用户------")
class User():
	def __init__(self, first_name, last_name, **user_info):
		self.first_name=first_name
		self.last_name=last_name
		self.user_name=self.first_name + " " + self.last_name
		self.user_infos=user_info
		
		#self.user_infos={}
		#for key,value in user_info.items():
		#	self.user_infos[key]=value
	
	def describe_user(self):
		print("\nUser's infomation is below...")
		print("--First name: " + self.first_name.title())
		print("--Last name: " + self.last_name.title())
		for key, value in self.user_infos.items():
			if key != 'age':
				print("--" + key + ": " + value)
			else:
				print("--age: " + str(value))

	def greet_user(self):
		print("\nHello " + self.user_name.title() + ",welcome!")

user1=User("fredrick","lily",gender='female',age=23)
user1.describe_user()
user1.greet_user()

user2=User("Green","Jim",gender='male',age=25)
user2.describe_user()
user2.greet_user()

user3=User("lyn","lucy",gender='female',age=29,homeland='Russia')
user3.describe_user()
user3.greet_user()
