# test 9-12 多个模块
import demo_9_12_user_module as user
import demo_9_12_admin_module as admin

new_admin=admin.Admin("jack","green",gender="male",phone="1234567498")
new_admin.privileges.show_privileges()

new_user=user.User("jim","coli",gender="male",age=32)
new_user.describe_user()
