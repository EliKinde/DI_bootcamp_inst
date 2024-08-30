year = int(input("Enter a year: "))

gg =  (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(gg, year, "is a leap year")
else:
    print(gg, year, "is not a leap year")
