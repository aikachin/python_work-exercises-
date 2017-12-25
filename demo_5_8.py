#!usr/bin/python
# -*- coding:utf-8 -*-

# test 5-8, 5-9
guest_names=['jack','hellen','tom','green','admin','david']
#guest_names=[]
if guest_names:
	for guest_name in guest_names:
		if guest_name != 'admin':
			print("Hello " + guest_name.title() + ",thank you for logging in again.")
		else:
			print("Hello admin,would you like to see a status report?")
else:
	print("We need to find some users!")



# test 5-10 检查用户名
current_users=['jack','hellen','Tom','green','admin','david']
current_users_lower=[]
new_users=['jack','john','tom','kate','admin','David']
new_users_lower=[]
if new_users and current_users:
#	for new_user in new_users:
#		new_users_lower.append(new_user.lower())
	for current_user in current_users:
		current_users_lower.append(current_user.lower())
	for new_user in new_users:		
		if new_user.lower() in current_users_lower:
			print("该用户名" + new_user + "已经被占用，请输入别的用户名")
		else:
			print("该用户名" + new_user + "可用")
