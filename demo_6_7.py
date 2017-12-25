#!usr/bin/python
# -*- coding:utf-8 -*-

# test 6-7 人
print("test 6-7 人")
friend_info1={'first_name':'jack',
	'last_name':'jones',
	'age':33,
	'city':'london',
	}
friend_info2={'first_name':'lily',
	'last_name':'jones',
	'age':30,
	'city':'paris',
	}
friend_info3={'first_name':'jim',
	'last_name':'greem',
	'age':20,
	'city':'tokyo',
	}
people=[]
#for num in range(0,3):
#手动把字典添加到列表people中
people.append(friend_info1)
people.append(friend_info2)
people.append(friend_info3)

for person in people:
	print(person)
	
# test 6-8 宠物
print("\ntest 6-8 宠物")
dog_info={'type':'dog','owner':'jack'}
cat_info={'type':'cat','owner':'kate'}
rabbit_info={'type':'rabbit','owner':'jim'}
pets=[]
pets.append(dog_info)
pets.append(cat_info)
pets.append(rabbit_info)
for pet in pets:
	print(pet)
	
	
# test 6-9 喜欢的地方
print("\ntest 6-9 喜欢的地方")
favorite_places={
	'jack':['china','australia'],
	'kate':['tokyo'],
	'hellen':['london','paris','shanghai'],
	}
for name, like_places in favorite_places.items():
	if len(like_places) < 2:
		print(name.title() + "'s favorite place is:")
	else:
		print(name.title() + "'s favorite places are:")
	for place in like_places:
		print("  " + place.title())



# test 6-10 喜欢的数字
print("\ntest 6-10 喜欢的数字")
favorite_numbers={
	'jim':['1','2','3'],
	'jack':['4','5'],
	'adel':['13'],
	'tom':range(2,10,2),
	}
for name, numbers in sorted(favorite_numbers.items()):
	if len(numbers) == 1:
		print(name.title() + "'s favorite number is:")
	else:
		print(name.title() + "'s favorite numbers are:")
	for number in numbers:
		print("  " + str(number))


# test 6-11 城市
print("\ntest 6-11 城市")
cities={
	'tokyo': {
		'country': 'japan',
		'population': '13.75 million',
		'fact': "Tokyo's fact...",
		},
	'beijing': {
		'country': 'china',
		'population': '21.7 million',
		'fact': "Beijing's fact...",
		},
	'paris': {
		'country': 'french',
		'population': '11.9 million',
		'fact': "巴黎的故事。。。",
		},
	}
for city, info in sorted(cities.items()):
	print(city.title() + "'s info is:")
	for attribute, details in info.items():
		if attribute == 'country':
			print("\t" + attribute.title() + " is: " + details.title())
		else:
			print("\t" + attribute.title() + " is: " + details)

