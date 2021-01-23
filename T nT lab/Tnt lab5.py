#%%
#1) Write a Python program to find the average of lowest 3 values in a dictionary.
mydict = {
  "marks1":44 ,
  "marks2": 39,
  "marks3":48,
  "marks4":33,
  "marks5": 47,
  "marks6": 50,
  "marks7": 41
}
values=[x for x in mydict.values()]
# SORTING in descending order
for i in range(0,len(values)):
   for j in range (i,len(values)):
      if values[i]<values[j]:
         temp=values[i]
         values[i]=values[j]
         values[j]=temp
average=(values[-1]+values[-2]+values[-3])/3
print(f"Dictionary={mydict}")
print(f"Average of lowest 3 values is {average}")
#%%
#2) WAP TO PRINT A DICT WITH 8 KEYS, UPDATE THE MIDDLE KEY AND DELETE SECOND LAST KEY  FROM RIGHT
mydict = {
  "name": "Debanjana",
  "branch": "CSSE",
  "year": 2018,
  "section": "4",
  "subject": "tnt",
  "sirname": "Mandal",
  "roll_no": "237",
  "day":"friday"
}
mydict2={"section": "5"}
mydict.update(mydict2)
del mydict["roll_no"]
print(str(mydict)+"dictionary")
#%%
#3)Write a Python program to get the frequency of the second last element  in a list.
s=0
mylist=[1,88,'o',7,9,[9,8],8,7,9,7,8,9,7,8]
f=mylist[-2]
for i in mylist:
    if i==f:
        s=s+1
print(s)        
#%%