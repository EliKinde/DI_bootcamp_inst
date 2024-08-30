names = ["Samus", "Cortana", "V", "Link", "Mario", "Cortana", "Samus", "Panty",
         "Adna"]

user_name = input("Enter your name: ")

if user_name in names:
    print(names.index(user_name))
else:
    print("your name is not in the list")


