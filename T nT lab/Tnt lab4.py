mydict = {
  "name": "Debanjana",
  "branch": "CSSE",
  "year": 2018
}
print(mydict)
#copy a dictionary into other dictionary
new_dict=mydict.copy()
print(new_dict)
# updating the contents of a dictionary
mydict2={"name": "Sneha"}
mydict.update(mydict2)
print(str(mydict)+"updated dictionary")
del mydict["name"]
print(str(mydict)+"deleted dictionary")
#%%
#WAP TO PRINT A DICT WITH 7 KEYS, UPDATE THE 3RD KEY AND DELETE SECOND LAST KEY  FROM RIGHT
mydict = {
  "name": "Debanjana",
  "branch": "CSSE",
  "year": 2018,
  "section": "4",
  "subject": "tnt",
  "sirname": "Mandal",
  "roll_no": "237"
}
mydict2={"year": "2019"}
mydict.update(mydict2)
print(str(mydict)+"updated dictionary")
del mydict["sirname"]
print(str(mydict)+"deleted dictionary")
#%%
#WAP to Check if a given key already exists in a dictionary
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
present(5)
present(9)
#%%
# dictionary comprehension .....(range starts from 0)
squares = {num: num*num for num in range(9)}
print(squares)
#%%
#factorial using dictionary 
def factorial(n): 
    if n < 0: 
        return 0
    elif n == 0 or n == 1: 
        return 1
    else: 
        fact = 1
        while(n > 1):
            fact *= n 
            n -= 1
        return fact 
    
fact = {x: factorial(x) for x in range(1,16)}
print(fact)
#%%
color_dict = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}

for key in sorted(color_dict):
    print("%s: %s" % (key, color_dict[key]))
#%%
#Filter a dictionary based on values
marks = {'Debanjana': 175, 'Sneha': 180, 'Arun': 165, 'Peter': 190}
print("Original Dictionary:")
print(marks)
print("Marks greater than 170:")
result = {key:value for (key, value) in marks.items() if value >= 170}
print(result)
#%%
#Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
dict={'1':['a','b'],'2':['c','d'],'3':['e','f']}
l1=dict.get('1')
l2=dict.get('2')
l3=dict.get('3')
for i in range (2):
    for j in range (2):
        for k in range (2):
            print(l1[i]+l2[j]+l3[k])
#%%            
    