

# test 7-4 比萨配料
prompt="\n请输入你需要的比萨配料： "
prompt+="\n(请输入'quit'来结束) "
peiliao=''
while True:
	peiliao = input(prompt)
	if peiliao != 'quit':
		print("我们会在比萨中添加这种配料：" + peiliao)
	else:
		break
