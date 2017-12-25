#!usr/bin/python
#-*- coding:utf-8 -*-

# test 6-1
friend_info={'first_name':'jack',
	'last_name':'jones',
	'age':33,
	'city':'london',
	}
print("My friend " +
	friend_info['last_name'].title() +
	"'s first name is " +
	friend_info['first_name'].title() +
	".He is " +
	str(friend_info['age']) +
	",and he lives in " +
	friend_info['city'].title() +
	".")

# test 6-2, 6-4
print("\n\ntest 6-2, 6-4")
print(range(1,10))
words={'circle':'A structure of codes that keep your program excuting the following actions until the expected condition come up.',
	'boolean_expression':'一段返回True或者False的代码表达式。',
	'range(x,y)':'表示一组在 x ~ y-1 之间的连续整数的列表.',
	'list':'Python中能够存储多个数据的一种结构的名称.',
	'元组':'Python中列表的一种，用来存储一组不需要改变（也无法修改）的数据的结构，但是可以重复定义（赋值）.',
	'字典':'以键值对的方式存储数据的结构名称',
	'操作列表':'可以使用for遍历，sorted()排序等',
	}

print("Circle means:" + "\n\t" + words['circle'] + "\n" +
	"Boolean_expression means:" + "\n\t" + words['boolean_expression'] + "\n" +
	"Range(x,y) means:" + "\n\t" + words['range(x,y)'] + "\n" +
	"List means:" + "\n\t" + words['list'] + "\n" +
	"元组 means:" + "\n\t" + words['元组']
	)

for key in sorted(words.keys()):
	print(key.title() + " means:\n\t" + words[key] + "\n")


# test 6-5 河流
rivers_countries={'nile':'egypt','changjiang':'china','amazon':'brazil','yellow':'china'}
for river,country in sorted(rivers_countries.items()):
	print("The " + river.title() + " runs through " + country.title() + ".")
print("\nThe rivers in dictionary are:")
for river in rivers_countries.keys():
	print("  " + river.title())

print("\nThe countries in dictionary are:")
for country in set(rivers_countries.values()):
	print("  " + country.title())


# test 6-6 调查
print("\ntest 6-6 调查")
name_list=['jack','tom','sarah']
favorite_languages={}
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
for name in name_list:
	print(name.title())
	if name in favorite_languages.keys():
		print("  Thank you for taking the poll!")
	else:
		print("  Please take our poll!")
