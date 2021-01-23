#PYTHON FUNCTION
#A function is a block of code which only runs when it is called.
#YOU CAN PASS DATA TO THE FUNCTION
#RETURN YOU THE RESULT
def my_function():
  print("Hello from a function")
#1. CREATE
#2. CALL
my_function()
#%%
#pass a function which display the country name
#Defining a function without any parameter
def my_function():
    c=str(input("Enter your country name"))
    print("My country name is: "+str(c))
my_function()    
#%%
# add a * before the parameter name to pass n arbitary arfument in the function
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("LALl", "TOM", "SIMA")
#%%
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1 = "RAM", child2 = "TOM", child3 = "LAL")
#%%
#Pass a list to a function
def my_function(food):
  for i in food:
    print(i)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
#%%
#RECURSION
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
#%% 1.
#create a function that can accept two arguments name and age and print their value
def my_func(name, age):
    print("Name is :" +str(name))
    print("Age is :"+str(age))

my_func("Debanjana", 21)
#%% 2.
#Create a function showEmployee() in such a way that it should accept employee name, and it’s salary and display both, and if the salary is missing in function call it should show it as 50000
def showEmployee(name, salary=50000):
    print("Employee", name, "salary is:", salary)

showEmployee("Kriti", 9000)
showEmployee("Kriti")
#%% 3.
#create multiplication table of 7 using recursion
def mul_table(N, i): 
    if (i > 10): 
        return
    print(N,"*",i,"=",N * i) 
    return mul_table(N, i + 1) 
N = 7
mul_table(N, 1) 
#%% 4.
#Write a recursive function to calculate the sum of numbers from 0 to 10
def calcSum(num):
    if num:
        return num + calcSum(num-1)
    else:
        return 0
res = calcSum(10)
print(res)
#%% 5.
#Generate a list of all even numbers between 2 to 100
start, end = 2, 100
# iterating each number in list 
for num in range(start, end + 1):    
    # checking condition 
    if num % 2 == 0: 
        print(num, end = " ")
#%% PATTERNS    
#1.
for  i in range(0,5):
   for j in range(0,5):
       print("*",end=" ")
   print()       
#%%
#2.
for i in range(65,70):
    print(chr(i)*5)
#%%
#3.
rows = 6
for num in range(rows):
    for i in range(num):
        print(num, end=" ") # print number
    # line after each row to display pattern correctly
    print(" ")       
#%%
#4.
l="PRABHU"
for i in range(7):
    print(l[0:i],end=" ")
    print()

#%%
#5.
l="EDCBA"
for i in range(5):
    print(l[0:5-i],end=" ")
    print()    
#%%    