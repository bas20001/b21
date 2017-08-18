from random import randint
class Die(object):
	def __init__(self,side=6):
		self.side = side
		
def roll_die():
	side = randint(1,6)
	print("Number is " + str(side))

time = 0
while time != 10:
	roll_die()
	time += 1
