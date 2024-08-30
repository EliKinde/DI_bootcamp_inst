user_word = input("Enter a String: ")
new_word = ""

i = 0
j = 0

while(j < len(user_word)):
    if user_word[i] == user_word[j]:
       j += 1
    elif ((user_word[i] != user_word[j]) or (j == len(user_word) -1)):
       new_word += user_word[i]

       i = j
       j += 1

new_word += user_word[j - 1]
print(f"user's word: {user_word} --> {new_word}")
