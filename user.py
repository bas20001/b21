class User(object):
	def __init__(self,first_name,last_name,age,sex,marriage):
		self.f_name = first_name
		self.l_name = last_name
		self.age = age
		self.sex = sex
		self.marriage = marriage
		self.login_attempts = 0
		self.privileges = ''
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
