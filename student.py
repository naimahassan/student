class Student:
	##constructor like initializing
	 def __init__(self,first_name,second_name,age):
			self.first_name=first_name
			self.second_name = second_name
			self.age=age

	 def full_name(self):
			return "your name  is {} {} , you are {} years old".format(self.first_name,self.second_name,self.age)

	 def year_of_birth(self):
			return 2019- self.age

	 def initials(self):
			a=self.first_name[0]
			b=self.second_name[0]
			c= a+b
			return c

