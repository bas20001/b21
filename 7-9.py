dreaming_trips = {}
switch = True
while switch:
	name = raw_input("\nWhat is your name?")
	dreaming_trip = raw_input("Which country would you want to trip?")
	
	dreaming_trips[name] = dreaming_trip
	repeat = raw_input("Would you like to let anther person respong?(yes/no)")
	if repeat == 'no':
		switch = False

print("\n--- Poll Results ---")
for name,dreaming_trip in dreaming_trips.items():
	print(name + " 's dreaming_trip is " + dreaming_trip + ".")
	

