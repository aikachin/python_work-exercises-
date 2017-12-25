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
