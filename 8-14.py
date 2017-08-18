def car_profile(name,company,**car_info):
	profile ={}
	profile['car_name'] = name
	profile['car_company'] = company
	for key,value in car_info.items():
		profile[key] = value
	return profile
car = car_profile('subaru', 'outback', color='blue', tow_package=True)
print(car)
