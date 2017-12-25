# test 8-6 城市名
def city_country(city, country):
	message=city.title() + ", " + country.title()
	return message
print(city_country('beijing','china'))

# test 8-7 专辑
print("\n\ntest 8-7 专辑")
def make_album(vocal, album_name, number_of_songs=''):
	if number_of_songs:
		album_info={
			'vocal': vocal.title(),
			'album_name': album_name,
			'number_of_songs': number_of_songs,
			}
	else:
		album_info={
			'vocal': vocal.title(),
			'album_name': album_name,
			}
	return album_info

album = make_album('miku','tell your world',1)
print(album)
album2 = make_album('rin','leyuan',)
print(album2)	
album3 = make_album('nagi','君が知らない物語',3)
print(album3)

# test 8-8 用户的专辑
print("\n\ntest 8-8 用户的专辑")
print("\n\ntest 8-7 专辑")
def make_self_album(vocal, album_name, number_of_songs=''):
	if number_of_songs:
		album_info={
			'vocal': vocal.title(),
			'album_name': album_name,
			'number_of_songs': number_of_songs,
			}
	else:
		album_info={
			'vocal': vocal.title(),
			'album_name': album_name,
			}
	return album_info

while True:
	print("请按提示完成专辑信息的输入：")
	print("(需要时退出时请输入'q')")
	
	vocal=input("输入歌手名字:")
	if vocal == 'q':
		break
	
	album_name=input("输入专辑名字:")
	if album_name == 'q':
		break
	
	number_of_songs=input("输入歌曲数目:")
	if number_of_songs == 'q':
		break
	
	if number_of_songs:
		album = make_self_album(vocal,album_name,number_of_songs)
	else:
		album = make_self_album(vocal,album_name)
	
	print(album)
