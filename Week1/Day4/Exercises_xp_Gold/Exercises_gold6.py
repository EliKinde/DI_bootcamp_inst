user_words = input("Enter Seven Words: ")
letter = input("Enter a single character: ")
words = user_words.split()
print(words)

for char in words:
    if letter in char:
        print(char.index(letter))
