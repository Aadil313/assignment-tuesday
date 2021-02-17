class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
class bus(Vehicle):
	def inhrt(self):
		print("maximum speed is",self.max_speed)
		print("mileage is",self.mileage)
	
mybus = bus(240,18)	
mybus.inhrt()

