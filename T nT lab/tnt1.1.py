#%%
lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Sum of elements in given list is :", sum(lst))   
#%%    
num = int(input("Enter a number: "))  
if num < 0:  
   print("Enter a positive number")  
else:  
   sum = 0  
   while(num > 0):  
       sum += num  
       num -= 1  
   print("The sum is",sum)      
#%%
for val in ("beautiful"):
    if(val=="t"):
        break
    print(val)
print("The End")    
#%%
year=int(input("Enter a year"))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("is a leap year")
       else:
           print(" is not a leap year")
   else:
       print(" is a leap year")
else:
   print(" is not a leap year")
#%%
x=int(input("Input a integer"))
y=int(input("Input a integer"))
if x > y:
        smaller = y
else:
        smaller = x
for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i   
print(hcf)        
#%%    