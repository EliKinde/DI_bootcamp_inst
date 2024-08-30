string_ten = input("Enter a string of ten char: ")

if len(string_ten) < 10:
    print("string not long enough")
elif len(string_ten) > 10:
    print("string too long")
else :
    print("perfect string")

#print the first and last characters.
print("\n",string_ten[0], string_ten[9] ,"\n")

space_char = ""
for charactor in string_ten:
    space_char += charactor
    print(space_char)


