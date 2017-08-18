def build_profile(first,last,**user_info):
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
user_profile = build_profile('Wang','Lihui',age = '28',
	sex = 'male', job = 'pythoner')
print(user_profile)
# b21
