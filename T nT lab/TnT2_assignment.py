#%%  1.
user1 = input("Enter name of User1")
user2 = input("Enter name of User2")
user1_answer = input("%s, do yo want to choose rock, paper or scissors?" % user1)
user2_answer = input("%s, do you want to choose rock, paper or scissors?" % user2)

def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
print(compare(user1_answer, user2_answer))
#%%  2.
string =input("Enter a string")
newString = "".join([i for i in string])
print(newString)
#%%  3.
def string_both_ends(str):  
  if len(str) < 2:  
    return ''  
  
  return str[0:2] + str[-2:]  
  
print(string_both_ends('kiituniversity'))  
print(string_both_ends('kiit'))  
print(string_both_ends('k')) 
#%%  4.
def add_string(str1):
  length = len(str1)

  if length > 2:
    if str1[-3:] == 'ing':
      str1 += 'ly'
    else:
      str1 += 'ing'

  return str1
print(add_string('ab'))
print(add_string('abc'))
print(add_string('string'))
#%%  5.
def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
result = find_longest_word(["happy", "exercises", "technology"])
print("\nLongest word: ",result[1])
print("Length of the longest word: ",result[0])
#%%