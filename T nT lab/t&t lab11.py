#class
#class variable
#data member
#methods
#....Program 1. below....1. A class called print1 is created and the __init__() method is used to initialize the value of the string to “”.
#2. The first method, get, takes the value of the string from the user.
#3. The second string, put, is used to print the value of the string.
#5. An object for the class called obj is created.
#6. Using the object, the methods get() and put() is printed.
#7. The value of the string is printed.

#yes __init__ is called by default when one object is created.
#All classes have a function called __init__(), which is always executed when the class is being initiated.
#it is generally used to initialized the object
class Computer:
    pass
obj = Computer()
#%%
def dance(self):
        return "{} is now dancing".format(self.name)
#%%
class Bird:
    
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        #super() when used in siblings class,gives access to the parent class....
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()
#%%        
#1. WAP that creates a class with a single method
class print1():
    def __init__(self):
        self.string=""
 
    def get(self):
        self.string=input("Enter string: ")
 
    def put(self):
        print("String is:")
        print(self.string)
 
obj=print1()
obj.get()
obj.put()
#%%
#2. WAP TO CREATE A CLASS  AND USE INATANCE VARIABLES
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)
    print("age is " + str(self.age))

p1 = Person("Debanjana", 21)
p1.myfunc()
#%%
#3. WAP TO COUNT NO. OF OBJECTS CREATED
class Student :

    # initialise class variable
    counter = 0

    # Constructor method
    def __init__(self,name,age) :

        # instance variable or object attributes
        self.name = name
        self.age = age

        # incrementing the class variable by 1
        # whenever new object is created
        Student.counter += 1

    # Create a method for printing details
    def printDetails(self) :
        print(self.name,self.age,"years old")

student1 = Student('Debanjana',22)
student2 = Student('Shreya',21)
student3 = Student('Shaurya',21)

# Print the total no. of objects cretaed 
print("Total number of objects created: ",Student.counter)
#%%
#4.USING CLASS CONCEPT IN  Python WAP to check a number is Palindrome number or not.
class Check :

    # Constructor
    def __init__(self,number) :
        self.num = number
        
    # define a method for checking number is Palindrome or not 
    def isPalindrome(self) :

        # copy num attribute to the temp local variable
        temp = self.num

        # initialise local variable result to zero
        result = 0

        # run the loop untill temp is not equal to zero
        while(temp != 0) :
            
            rem = temp % 10

            result =  result * 10 + rem

            # integer division
            temp //= 10

        # check result equal to the num attribute or not
        if self.num == result :
            print(self.num,"is Palindrome")
        else :
            print(self.num,"is not Palindrome")

if __name__ == "__main__" :
    
    # input number
    num = 151
    
    # make an object of Check class
    check_Palindrome = Check(num)
    
    # check_Palindrome object's method call
    check_Palindrome.isPalindrome()
    
    num = 127
    check_Palindrome = Check(num)
    check_Palindrome.isPalindrome()
#%%
#5. Python program to add two distances
class Distance:
    def GetDistance(self):
        self.__cm=int(input("Enter CM: "))
        self.__m=int(input("Enter M: "))
        self.__km = int(input("Enter KM: "))

    def PutDistance(self):
        print(self._km,self.m,self._cm)

    def _add_(self, T):
        R=Distance()
        R._cm=self.cm+T._cm
        R._m=self.m+T._m
        R._km = self.km + T._km
        R._m=R.m+(R._cm//100)
        R._cm=R._cm%100
        R._km=R.km+(R._m//1000)
        R._m=R._m%1000

        return R

D1=Distance()
D2=Distance()

print("Enter first distance")
D1.GetDistance()

print("Enter second distance")
D2.GetDistance()

D3=D1+D2

print("The sum of both distance is")
D3.PutDistance()
#%%