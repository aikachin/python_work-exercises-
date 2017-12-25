# 打印三明治
def describe_sandwiches(*info_list):
	print("\n顾客点的三明治包含以下辅料：")
	for info in info_list:
		print("-" + info.title())

def build_profile(first_name,last_name,**user_info):
	profile={}
	profile['first_name']=first_name
	profile['last_name']=last_name
	for key,value in user_info.items():
		profile[key]=value;
	return profile
