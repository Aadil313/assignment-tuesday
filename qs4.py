class part:
	def __init__(self):
		self.str1 = ""
	def get_string(self):
		self.str1 = input("enter")
	def print_str(self):
		print(self.str1.upper())
str1 = part()
str1.get_string()
str1.print_str()