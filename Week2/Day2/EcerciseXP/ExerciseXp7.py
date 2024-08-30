import random

#def main():
#    def get_random_temp():
#        Celsius = random.randint(-10, 40)
#        return Celsius
#    degrees = get_random_temp()
#    print(f"The temperature right now is {degrees} Celsius")
#
#    if -10 < degrees < 0:
#        print("Brr, that's freezing! Wear some extra layers tody")
#    elif 0 < degrees < 16:
#        print("Quit chilly! Don't forget your coat")
#    elif 16 < degrees < 23:
#        print("The seasons is Autumn")
#    else:
#        print("is vary hot outside drike Water")
#
#main()


def main():
    Celsius = random.randint(-10, 40)
    def get_random_temp(season):
        if -10 < season < 0:
            print("The Season is Winter")
        elif 0 < season < 16:
            print("The Season is Spring")
        elif 16 < season < 23:
            print("The seasons is Summer")
        else:
            print("The Season is Autumn")
    get_random_temp(Celsius)
    print(f"The temperature right now is {Celsius} Celsius")


main()
