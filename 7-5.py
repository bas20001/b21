age = ""
print("Please input your age to know how much")
print("If you want to exit please input 'quit'")
age = raw_input("\nPlease input your age: ")
while True:
	if age == "quit" :
		break
	elif int(age) < 3:
		print("You can free to see the film")
	elif int(age) <= 12:
		print("You need to pay 10 dollars")
	else :
		print("You need to pay 15 dollars")
