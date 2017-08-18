class Restaurant(object):
	def __init__(self,restaurant_name,cuisine_type):
		self.name = restaurant_name
		self.type = cuisine_type
		self.number_served = 0
	
	def describe_restaurant(self):
		print("This restaurant name is " + self.name
			+ " and its cuisine_type is " + self.type + '.')
	def open_restaurant(self):
		print(self.name + " now is openning")
	
	def set_number_served(self,number_served):
		self.number_served = number_served
	def read_number_served(self):
		print("There is " + str(self.number_served) + 
			" people to this restaurant.")
	def increase_number_served(self,number_served):
		self.number_served += number_served

class IceCreamStand(Restaurant):
	def __init__(self,restaurant_name,cuisine_type):
		super(IceCreamStand,self).__init__(restaurant_name,cuisine_type)
	
	def flavors(self):
		print("My best flavors in " + self.name.title() + " is " + 
		self.type)
pizza_restaurant = Restaurant('pizza_hut','france pizza')
pizza_restaurant.describe_restaurant()
pizza_restaurant.open_restaurant()
pizza_restaurant.set_number_served(45)
pizza_restaurant.increase_number_served(10)
pizza_restaurant.read_number_served()
pizza_restaurant.increase_number_served(10)
pizza_restaurant.read_number_served()
menglong = IceCreamStand('menglong','strawberry')
menglong.flavors()

