
class Privileges(object):
	def __init__(self,privileges=''):
		self.privileges = privileges
	def show_privileges(self):
		print("The Privileges can do " + str(self.privileges))
