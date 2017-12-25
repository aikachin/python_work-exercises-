# test 7-8 熟食店, 7-9 五香烟熏牛肉
sandwich_orders=['鸡肉三明治','火腿三明治','pastrami','海苔三明治','pastrami']
finished_sandwiches=[]
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
	print("很抱歉，熟食店的 pastrami 卖完了")

for sandwich in sandwich_orders:
	print("I made your " + sandwich)
	finished_sandwiches.append(sandwich)

print(sandwich_orders)
print("\nAll sandwiched are finished: ")
finished_sandwich=''
while finished_sandwiches:
	finished_sandwich=finished_sandwiches.pop()
	print("\t" + finished_sandwich)

# test 7-10 梦想的度假胜地
print("\n# test 7-0 梦想的度假胜地")
poll_message="\nIf you could visit one place in the world, where would you go?"
poll_tip="\n(enter 'quit' to end the poll, the following question is the same as this)\n\t"
poll_message+=poll_tip
poll_message2="\nPlease input your age:"
poll_message3="\nPlease input your gender:"

poll_results=[]
flag=True
count=0
place=''
age=''
gender=''
while flag:
	poll_temp={}

	place=input(poll_message)
	if place != 'quit':
		poll_temp['place']=place
	else:
		flag=False
		continue
		
	age=input(poll_message2)
	if age != 'quit':
		poll_temp['age']=age
	else:
		flag=False
		continue

	gender=input(poll_message3)
	if gender != 'quit':
		poll_temp['gender']=gender		
	else:
		flag=False
		continue
		
	#print(poll_temp)
	#print(poll_results)
	poll_results.append(poll_temp)
	#print(poll_results)

print("\nThank you for taking our poll!")

print("\n-----调查结果如下-----")
while poll_results:
#for poll_result in poll_results:
	poll_result=poll_results.pop()
	#for key in poll_result:
	print("    gender: " + poll_result['gender'])
	print("    age: " + poll_result['age'])
	print("    place: " + poll_result['place'])
	print("--")

