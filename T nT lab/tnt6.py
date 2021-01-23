#find the square and cube of a numbe
choice = input('enter1 for square 2 for cube depend upon your choice: ')

num = int(input('enter a number'))

if choice=='1':
    
    print('Square of given number is ',num**2)
    
elif choice=='2':
    
    print('Cube of given number is ',num*num*num)
    
else:
    
    print('Invalid choice')
#%%
#WAP TO MATCH WHETHER YOUR GUESED VALUES ARE SAME AS THAT OF SCORED VALUES AND ALSO FIND THE GRADES OF SCORED VALUES    
g=int(input("Enter your guessed value"))
s=int(input("Enter your scored value"))
if(g==s):
    print("Guessed right")
if(g>90):
    print("Grade O")
elif ((g>80)and(g<90)):
    print("Garde E")
elif ((g>70)and(g<80)):
    print("Garde A")
elif ((g>60)and(g<70)):
    print("Garde B")    
else:
    print("Grade C")    

#%%
#WAP TO PREPARE A SHOPPING LIST, ATLEAST 10 INPUTS AND TO DISPLAY THE ITEM WHICH HAS MAX PRIORITY    
#least number is maximum priority
dict = {}
n=int(input("Enter the no. of items you wish to add : "))
i=1
while i <=n:
    p=int(input("Enter the priority(1- max, 10-least) : "))
    item=input("Enter the item : ")
    dict[p]=item
    i+=1

print("Max Priority item is : ",dict[1])
#%%
#WAP TO CALCULATE THE COST OF FILLING A CYLINDER (USER WILL GIVE THE DIM
#@ 235/Cu.m and also the time to fill if it takes 14minutes to fill 1 cu.
r=float(input("Please enter the radius "))
h=float(input("Please enter the height "))
vol=3.14*r*r*h
cpm=float(input("Enter the cost per cubic metre:"))
cost=vol*cpm
print("The cost of filling your cylinder is: Rs.",cost)
print("The time taken to fill your cylinder:",str(vol*14),"mins")
#%%
#Wap to store a student list with all the details of a student and give warning to students with attendance less than 60
dict = {'name':["Debanjana", "Aparna", "Sumedha", "Tania"], 
        'degree': ["BTech", "BCA", "MTech", "MBA"], 
        'Attendance':[90, 40, 80, 23]} 

lst=[]

for i in range(4):
    if int(dict['Attendance'][i])<=60:
        lst.append(i)
        
print("Warning To:")
for i in range(len(lst)):
    print(dict['name'][lst[i]])
#%%