switch = True	
pass_button = ""
tall = ""
weight = ""
attack = ""
defend = ""
hp = ""
enemy_attack = ""
enemy_defend = ""
enemy_hp = ""
print("Welcome to my first game! If you want to exit input 'quit'")
pass_button = raw_input("any key to continue")

print("Enjoy it")
pass_button = raw_input("any key to continue")

print("Creat a character")
pass_button = raw_input("any key to continue")
print("choose your sex")
sex = raw_input("Please choose your sex 'man' or 'women'.")
if sex == "man":
	print("Please tell me how tall 'cm' you have ? Man.")
	
	tall = raw_input("please input your tall: ")
	
	attack = int(tall) * 1.250 
    
	enemy_attack = int(attack) * 0.75 
    
	print("Please tell me your weight'kg'.Man.")
    
	weight = raw_input("please input your weight :")
    
	defend = int(weight) * 2.30
    
	enemy_defend = int(defend) * 0.75
    
	hp = int(attack) + int(defend)
    
	enemy_hp = int(hp) * 0.3
	print("Now tell me what your name")
	name = raw_input("input your name : ")
	print("OK! " + name.title() + ". Welcome to the battle.")
	pass_button = raw_input("any key to continue")
	print("Your hp is " + str(hp) + ".\nYour attack is " + str(attack))
	print("Your defend is " + str(defend))
	Start_button = raw_input("Are you ready? (yes/no)")
	if start_button != 'yes':
		Start_button = raw_input("Are you ready? (yes/no)")
	print("One day " + name + " come to a battlefield")
	print("Your first enemy have appearance")
		
	
		

		


	
