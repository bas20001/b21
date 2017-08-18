class User(object):
	def __init__(self,first_name,last_name,age,sex,marriage):
		self.f_name = first_name
		self.l_name = last_name
		self.age = age
		self.sex = sex
		self.marriage = marriage
		self.login_attempts = 0
		
	def describe_user(self):
		print('The user name is ' + self.f_name.title() + 
			self.l_name + '.\nsex is ' + self.sex + ' and age is '
			 + str(self.age)) 
	def greet_user(self):
		if self.sex == 'male' :
			print('Hello Mr. ' + self.f_name.title() + ' Welcome to my '
				'website')
		else :
			if self.marriage == 'false':
				print('Hello Miss. ' + self.f_name.title() + ' Welcome to my'
				'website')
			else :
				print('Hello Mrs. ' + self.f_name.title() + ' Welcome to my'
				'website')
	def set_login_attempts(self,login_attempts):
		self.login_attempts = login_attempts
	def increase_login_attempts(self,login_attempts):
		self.login_attempts += login_attempts
	def reset_login_attempts(self,login_attempts):
		login_attempts = 0
	def read_login_attempts(self):
		print("Username " + self.f_name.title() + "'s login_attempts "
			'is ' + str(self.login_attempts))

class Privileges(object):
	def __init__(self,privileges=''):
		self.privileges = privileges
	def show_privileges(self):
		print("The Privileges can do " + str(self.privileges))
	

wang = User('wang','lihui',28,'male','true')
zhang = User('zhang','yi',28,'female','false')
wang.describe_user()
zhang.greet_user()
wang.set_login_attempts(10)
wang.read_login_attempts()
wang.increase_login_attempts(1)
wang.read_login_attempts()
wang = Privileges(["can add post","can delete post","can ban user"])
wang.show_privileges()

