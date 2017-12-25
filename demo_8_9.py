# test 8-9 魔术师
def show_magicians(magicians):
	for magician in magicians:
		print(magician)
	
magician_list=['magician1','magician2','magician3']
show_magicians(magician_list)

# test 8-10 了不起的魔术师
print("\n\n8-10 了不起的魔术师")
def make_great(magicians):
	"""
	在8-9中的 魔术师 列表中的每一位魔术师名字中加入'the Great'字样
	"""
	count=0
	while count < len(magicians):
		magicians[count] = "the Great " + magicians[count]
		count+=1

make_great(magician_list)
show_magicians(magician_list)

# test 8-11 不变的魔术师
print("\n\n8-11 不变的魔术师")
#把魔术师列表复原
magician_list=['magician1','magician2','magician3']
magicians_after=[]
def make_great_after(magicians):
	count=0
	while count < len(magicians):
		magicians_after.append("the Great " + magicians[count])
		count+=1

make_great_after(magician_list[:])
show_magicians(magician_list)
show_magicians(magicians_after)
