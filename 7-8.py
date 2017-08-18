sandwich_orders = ['bacon','banana','xigua']
orders = []
finished_sandwiches = []
print("Today's sandwich have " + str(sandwich_orders))
print("Please input the number which sandwich did you want")
print("If you want to exit please input 'quit'")
switch = True
while switch != False :
	order = raw_input("\nPlease input your order: ")
	if order == "quit":
		switch = False
	elif order in sandwich_orders :
		print("We will made: " + order + " sandwich for you")
		order = sandwich_orders.remove(order)
		finished_sandwiches.append(order)
	elif order == "stock":
		print(sandwich_orders)
	else :
		print("Sorry we have not " + order + " sandwich!")
		
