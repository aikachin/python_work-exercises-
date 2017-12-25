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

