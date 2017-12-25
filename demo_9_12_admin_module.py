from demo_9_12_user_module import User
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
