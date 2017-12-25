# test 8-1 消息
def display_message():
	print("本章学习了函数的使用。")

display_message()

# test 8-2 喜欢的图书
def favorite_book(title):
	print("\nOne of my favorite book is " + title + ".")

favorite_book('Alice in Wonderland')

def my_pet(pet_name, pet_type='dog'):
	"""打印宠物类型和宠物名字的函数"""
	print("\nI have a " + pet_type + ".")
	print("My " + pet_type + "'s name is " + pet_name.title() + ".")

my_pet('kate', 'cat')


# test 8-3 T恤
print("\n\ntest 8-3 T恤------")
def make_shirt(size, word):
	print("  T恤的尺码是：" + size + ", 字样是：" + word + ".")
print("使用位置实参调用make_shirt()函数:")
make_shirt('XL','Universal')
print("使用关键字实参调用make_shirt()函数:")
make_shirt(size='XL',word='Universal')


# test 8-4 大号T恤
print("\n\ntest 8-4 大号T恤------")
def make_shirt2(size='L', word='I love Python'):
	print("开始制造如下样式的T恤。尺码是：" + size + ", 字样是：" + word + ".")
make_shirt2()
make_shirt2(size='M')
make_shirt2(word='123')


# test 8-5 城市
print("\n\ntest 8-5 城市------")
def describe_city(city, country='Iceland'):
	print(city.title() + " is in " + country.title() + ".")
describe_city('Reykjavik')
describe_city('beijing', 'china')
describe_city('Washington', country='U.S.A')
