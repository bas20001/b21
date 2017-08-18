file_path = 'C:\Python27\learning_python.txt'

with open(file_path) as file_object:
	pi_line = ''
	
	lines = file_object.readlines()
	
	for line in lines:
		
		pi_line += line.replace('Python','C') + '\n'
		
print(pi_line)
	
	
