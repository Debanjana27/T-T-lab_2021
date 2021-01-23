nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
#%%
#power of x^n
def power(x, y): 
  
    if (y == 0): return 1
    elif (int(y % 2) == 0): 
        return (power(x, int(y / 2)) *
               power(x, int(y / 2))) 
    else: 
        return (x * power(x, int(y / 2)) *
                   power(x, int(y / 2))) 
  
x =int(input());
y = int(input());
print(power(x, y))        
#%%
#S=1+(1+2)+(1+2+3)+...+(1+2+3+...+n)
def sumOfSeries(n): 
    return sum([i*(i+1)/2 for i in range(1, n + 1)]) 
  
# Driver Code  
if __name__ == "__main__": 
    n = 10
    print(sumOfSeries(n)) 
#%%
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Enter which operation would you like to perform?")
ch = input("Enter any of these char for specific operation +,-,*,/: ")

result = 0
if ch == '+':
    result = num1 + num2
elif ch == '-':
    result = num1 - num2
elif ch == '*':
    result = num1 * num2
elif ch == '/':
    result = num1 / num2
else:
    print("Input character is not recognized!")

print(num1, ch , num2, ":", result)
#%%
import cmath

a = 1
b = 5
c = 6
d = (b**2) - (4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))
#%%    