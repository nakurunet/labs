class Car(object):
	"""Class car.  Car can be trailer or saloon. Car should have 4 doors except Porsche or Koenigsegg.Car should have 4 wheels except trailer. Car name and model should be instance property of Car. Car model default should be GM. Car name default should beGeneral. """
	#name = "General"
	#model = "GM"
	#v_type = None
	def __init__(self, name="General",model="GM", v_type=0 ):
		self.name = name
		self.model = model
		self.v_type = v_type
		
		self.speed = 0
		self.num_of_doors = 4 if not(name =='Porshe' or name == 'Koenigsegg') else 2
		self.num_of_wheels = 8 if v_type == "trailer" else 4
		
	
	def is_saloon(self):# Check car type
		if self.v_type != "trailer":
			self.v_type = "saloon"
			return True #True if is saloon
		return False
	
	def drive(self, moving_speed):# Check move speed 
		if moving_speed == 3:
			self.speed = 1000
		elif moving_speed == 7:
			self.speed = 77
		return self #return speed
