fruits = input("Enter your Favorite Frutis: eg: 'apple mango cherry'")

fruits_fav = fruits.split()

user_fruits = input("Enter name of any fruit: ")

if user_fruits in fruits_fav:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")
