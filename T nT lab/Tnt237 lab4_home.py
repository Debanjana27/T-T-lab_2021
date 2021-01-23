#1.Write a Python program to find the average of highest 3 values in a dictionary.
import random
dictionary={x:random.randint(x,100) for x in range(1,21) }
values=[x for x in dictionary.values()]
# SORTING in ascending order
for i in range(0,len(values)):
   for j in range (i,len(values)):
      if values[i]>values[j]:
         temp=values[i]
         values[i]=values[j]
         values[j]=temp
average=(values[-1]+values[-2]+values[-3])/3
print(f"Dictionary={dictionary}")
print(f"Average of highest 3 values is {average}")

#%%
#2.Write a Python program to get the top FIVE items in an inventry.
mydict = {
  "marks1":44 ,
  "marks2": 39,
  "marks3":48,
  "marks4":33,
  "marks5": 47,
  "marks6": 50,
  "marks7": 41
}
print(mydict)
values=[x for x in mydict.values()]
for i in range(0,len(values)):
    for j in range(i,len(values)):
        if values[i]<values[j]:
            temp=values[i]
            values[i]=values[j]
            values[j]=temp
print("top 5 values:"+str(values[:5]))

#%%
#3.Write a Python program to replace dictionary values with their ASCII values
dictionary={'c':'c',9:'9','a':'a','z':'z',1:'1'}
print(f'Original Dictionary:\n {dictionary}')
for i in dictionary.keys():
    dictionary[i]=ord(dictionary[i])
print(f'Dictionary with ASCII values:\n {dictionary}')


#%%
#4.Write a Python program to create a dictionary of keys p, q, and r where each key has as value a list from 101-120, 201-220, and 301-320 respectively. Display the seventh (both from beginning and end)value of each key from the dictionary
dicPQR={'p':[x for x in range(101,121)],'q':[x for x in range(201,221)],'r':[x
for x in range(301,321)]}
for i in dicPQR.keys():
    print("{}: Seventh item fomm the Beginning is {}, and from the End is {}".format(i,dicPQR[i][6],dicPQR[i][-7]))