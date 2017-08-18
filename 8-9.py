def show_magicians(names):
	for name in names :
		msg = name + " who is a great magician!"
		print(msg)
def make_great(uncurrent_names,current_names):
	while uncurrent_names :
		make_greatnames = uncurrent_names.pop() + 'the Great '
		current_names.append(make_greatnames)
		
uncurrent_names = ['apple','zona','liki']
current_names = []
make_great(uncurrent_names[:],current_names)
show_magicians(current_names)
show_magicians(uncurrent_names)
		
