request_garnishs = []
print("Please input which garnish you would like")

print("If you finished please input 'quit' to close the app")
print("If you want to show all your garnishs please input 'show all'")
switch = True
while switch != False:
	request_garnish = raw_input("please input:")
	if request_garnish == "quit":
		switch = False
	elif request_garnish == "show all":
		print("You have already add " + str(request_garnishs) + "to your pizza")	
	else :
		request_garnishs.append(request_garnish)
		print("We will add " + request_garnish + " to your pizza")
