# test 9-11 导入Admin类
from demo_9_11_user_module import User, Admin, Privileges
new_admin=Admin("jack","green",gender="male",phone="1234567498")
new_admin.privileges.show_privileges()
