
toppings= []

while  True:
    user_toppings = input("Enter your toppings that you want? ")
    print(f"you add {user_toppings} to the Pizza")
    toppings.append(user_toppings)
    if user_toppings == "quit":
        toppings.pop()
        break


print(toppings)
price = 10 + 2.5 * len(toppings)
print(f"The price is {price}$")
