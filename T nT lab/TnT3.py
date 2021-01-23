# list=>ordered,indexed,changeable,contain diff data types......
kiit = ["cse", "csse", "csce"]
#slicing
my_list=[1,2,3,4,5,6,7,8]
my_list[2:5]
#add or change element of a list
kiit[1]="ece"
print(kiit)

a = [2, 4, 6, 8]
a[1]=9
print(a)
#    append() - Add an element to the end of the list
 #   extend() - Add all elements of a list to the another list
  #  insert() - Insert an item at the defined index
   # remove() - Removes an item from the list
    #pop() - Removes and returns an element at the given index
#    clear() - Removes all items from the list
 #   index() - Returns the index of the first matched item
  #  count() - Returns the count of the number of items passed as an argument
   # sort() - Sort items in a list in ascending order
    #reverse() - Reverse the order
#%%  1.
#maximum element in a list
list1=[1,2,34,22,5,3]

max = list1[0] 
for x in list1: 
        if x > max : 
             max = x 
print(max)
#%%  2.
#sum of list elements
total = 0
list1 = [11, 5, 17, 18, 23] 
for ele in range(0, len(list1)):
    total = total + list1[ele]
print("Sum of all elements in given list: ", total)
#%%  3.
#Write a Python program to get a list sorted in decreasing order 
my_list = [-15, -26, 15, 1, 23, -64, 23, 76]
new_list = []
while my_list:
    max = my_list[0]  
    for x in my_list: 
        if x>max:
            max = x
    new_list.append(max)
    my_list.remove(max)    

print(new_list)
#%%  4.
#Write a Python program to clone or copy a list
original_list = [10, 22, 44, 23, 4]
new_list = list(original_list)
print(original_list)
print(new_list)
#%%   5.
#Write a Python program to get the frequency of the elements in a list.
list=[1,2,3,4,55,3,3,2,4,6]
freq={ }
for i in list :
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)
#%%  6.
#WAP TO  SEPARATE THE STRING VALUES FROM A LIST WITH DIFFRENT DATATYPES AND ALSO COUNT THEIR FREQUENCY
list=["happy","technology","python",1,3,4,"apple",98.0]
Stringele=[]
freq={ }
for i in list :
    if type(i)== str:
        Stringele.append(i)
        if i in freq:
           freq[i]+=1
        else:
           freq[i]=1
print(Stringele)
print(freq)
#%%  7.
#WAP TO JOIN 2 LIST AND FIND THE SMALEST  ELEMENT FROM THE THIRD LIST
list1 = [5,7,9]
list2 = [1,2,3]
list3 = list1 + list2
min = list3[0] 
for x in list3: 
        if x < min : 
             min = x 
print(max)
#%%