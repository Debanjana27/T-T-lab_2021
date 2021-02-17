#1.Patterns
def pattern(n):
    for i in range(n,0,-1):
        print("*"*i+' '*((n-i)*2)+'*'*i)
num=int(input("Enter num :"))
pattern(num)        
#%%
#2. wap to find whether a number is perfect number using function   
def Perfect_Number(Number):
    Sum = 0
    for i in range(1, Number):
        if(Number % i == 0):
            Sum = Sum + i
    return Sum        
Number = int(input("Please Enter any number: "))
if (Number == Perfect_Number(Number)):
    print("\n %d is a Perfect Number" %Number)
else:
    print("\n %d is not a Perfect Number" %Number)
#%%
#3. wap to find whether a number is Armstrong number using function  
def Armstrong_Number(Number):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    return sum    
num = int(input("Enter a number: "))
if num == Armstrong_Number(num):
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")    
#%%
#4.Fahrenheit to celcius conversion using functions
def FahToCel(f):
    return (f-32)/1.8

fah = float(input("Enter Temperature in Fahrenheit: "))

cel = FahToCel(fah)

print("Equivalent Temperature in Celsius = ",cel)   
#%%
#5.total surface a cuboid using functions of the given dimension
def surfaceAreaCuboid( l , h , w ): 
    return (2 * l * w + 2 * w * h + 2 * l * h) 
  
# driver function 
l = 3.5
h = 4
w = 2 
print("Total Surface Area =", surfaceAreaCuboid(l, h, w))
#%%
#6.Patterns
def fun(n):
    c=1
    for j in range(1, n + 1):
        for k in range(n-j):
            print(" ",end="")
        for i in range(1, j + 1):
            print(c, end = " ")
        c= c+2 
        print("")
n= int(input ("Enter the no. of rows:"))
fun(n)
#%%
#7.
def pat(n):
    for i in range(n,0,-1):
        print('*'*i+' '*((n-i)*2)+'*'*i)
    for i in range(n+1):
        print('*'*i+' '*((n-i)*2)+'*'*i)
pat(5)
#%%
#8.
def pattern(n):
    num=1
    for i in range(1, n):
        for j in range(n-i):
            print(" ", end="")
        for j in range(65, 65+num):
            a = chr(j)
            print(a, end="")
        print()
        num+=2
pattern(int(input("No. of lines: ")))
#%%
#9.Convert decimal to binary
def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')
dec = int(input("Enter the number"))
convertToBinary(dec)
print()   
#%%
#10.Find ascii value of given input using function
def to_ascii(x):
  l=[ord(c) for c in x]
  return l
list_of_ascii=to_ascii("Debanjana")
print(list_of_ascii)
#%%
#11.
def compute_lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm
num1 = int(input("Enter num1"))
num2 = int(input("Enter num2"))
print("The L.C.M. is", compute_lcm(num1, num2))
#%% 