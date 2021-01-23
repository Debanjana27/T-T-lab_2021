#%%  1.
# fetch a datatype
x=16.0
print(type(x))
#%%  2.
# remove characters in a string except alphabets
istring=str(input("Enter a string"))
str2=" "
for i in istring:
    if (ord(i)>=65 and ord(i)>=90) or (ord(i)>=97 and ord(i)>=122):
        str2+=i
print("Alphabeta are:"+ str2)
    
#%%  3.
#pallindrome or not
s= str(input("Enter a string"))
rev=s[::-1]
if s==rev:
    print("pallindrome")
else:
    print("not pallindrome")
#%%  4.
#sort srtings in dictionary order
my_str = ["happy","we","colour","pallindrome"]
my_str.sort()
print("Dictionary order:")
print(my_str)    
#%%  5.
#find frequency of character
string=str(input("Enter a string"))
freq={ }
for i in string :
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)
#%%
            
        
   