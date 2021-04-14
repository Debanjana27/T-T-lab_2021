#Inheritance
#Single Inheritance
#When a child class inherits only a single parent class.
#multiple inheritance
#when a child class inherits from more than one parent class.
#Multilevel Inheritance
#When a child class becomes a parent class for another child class.
#Hierarchical inheritance involves multiple inheritance from the same base or parent class.
#%%
#Single Inheritance
class Parent:
     def func1(self):
          print("This function is in parent class.")
class Child(Parent):
     def func2(self):
          print("This function is in child class.")
object = Child()
object.func1()
object.func2()
#%%
#Multiple
class Mother:
    mothername = ""
    def mother(self):
        print(self.mothername)
class Father:
    fathername = ""
    def father(self):
        print(self.fathername)
class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
s1 = Son()
s1.fathername = "RAJESH"
s1.mothername = "SHREYA"
s1.parents()
#%%
#Multilevel
class Grandfather:

	def __init__(self, grandfathername):
		self.grandfathername = grandfathername
class Father(Grandfather):
	def __init__(self, fathername, grandfathername):
		self.fathername = fathername
		Grandfather.__init__(self, grandfathername)
class Son(Father):
	def __init__(self,sonname, fathername, grandfathername):
		self.sonname = sonname
		Father.__init__(self, fathername, grandfathername)
	def print_name(self):
		print('Grandfather name :', self.grandfathername)
		print("Father name :", self.fathername)
		print("Son name :", self.sonname)
s1 = Son('SOHAM', 'SAURAV', 'NARESH')
print(s1.grandfathername)
s1.print_name()
#%%
#1. Hierarchical inheritance
class Parent:
	def func1(self):
		print("This function is in parent class.")
class Child1(Parent):
	def func2(self):
		print("This function is in child 1.")
class Child2(Parent):
	def func3(self):
		print("This function is in child 2.")
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()
#%%
#2.
# python-inheritance.py


