import random

def randomly_number(number_random):
    number_one = random.randint(1, 100)
    if number_one == number_random:
        print("Success they Equal")
    if number_one != number_random:
        print("Fail they not Equal")

    print(number_one, number_random)

number_random = random.randint(1, 100)

randomly_number(number_random)

