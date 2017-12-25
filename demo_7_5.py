# test 7-5 电影票

print("\n使用break结束循环.....")
prompt="\n请输入你的年龄决定电影票价格："
prompt+="\n(请输入'quit'来结束) "
age=""
while True:
	age = input(prompt)
	if age != 'quit':
		if age != "" and int(age) >= 0:
			if int(age) < 3:
				print("未满3岁可以免费观看。")
			elif int(age) <= 12:
				print("票价为10美元。")
			elif int(age) > 12:
				print("票价为15美元。")
		else:
			print("您的输入有误，请输入正确的岁数！")
	else:
		break

print("\nwhile 条件测试结束循环.....")
age=""
while age != 'quit':
	age = input(prompt)

	if age != "" and int(age) >= 0:
		if int(age) < 3:
			print("未满3岁可以免费观看。")
		elif int(age) <= 12:
			print("票价为10美元。")
		elif int(age) > 12:
			print("票价为15美元。")
	else:
		print("您的输入有误，请输入正确的岁数！")


print("是指标记来结束循环.....")
age=""
flag=True
while flag:
	age = input(prompt)
	if age != 'quit':
		if age != "" and int(age) >= 0:
			if int(age) < 3:
				print("未满3岁可以免费观看。")
			elif int(age) <= 12:
				print("票价为10美元。")
			elif int(age) > 12:
				print("票价为15美元。")
		else:
			print("您的输入有误，请输入正确的岁数！")
	else:
		flag = False
