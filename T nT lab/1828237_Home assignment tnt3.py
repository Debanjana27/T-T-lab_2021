#%%                                                                                                        #Home Assignment
1
#Write a Python program to check whether a list contains a sublist. 
l = [2,4,3,5,7]
s = [4,3]
sset = False
if s == []:
    sset = True
elif s == l:
    sset = True
elif len(s) > len(l):
    sset = False
else:
    for i in range(len(l)):
        if l[i] == s[0]:
            n = 1
            while (n < len(s)) and (l[i+n] == s[n]):
                n += 1
            if n == len(s):
                sset = True
if sset:
    print("Yes It's is A subset")
else:
    print("Not A SubSet")

#%%

2
#Write a Python program to find common items from two lists.
l = [2,4,3,5,7]
s = [4,3]
print(set(l) & set(s))

#%%

3
#Write a Python program to split a list of 20 elements after every 4th element
S=['a','b','c','d','e','f','g','h','i','jack','k','l','m',3,'o','p']
step=4
[S[i::step] for i in range(step)]
#%%

