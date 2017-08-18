filename = 'guest.txt'
switch = True
guest_name = ''
while switch != False:
	guest_name = raw_input('Input your name ! or input q to quit\n')
	if guest_name == 'q':
		switch = False
	else :
		print("Welcome to my website" + guest_name.title())
		with open(filename,'w') as file_object:
			file_object.write(guest_name.lower())



