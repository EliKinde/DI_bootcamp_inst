birthdate = input("Enter your Birthday: (dd/mm/yyyy)\n")

year = int(birthdate[6:10])

age = 2024 - year

age_str = int(str(age)[1])



candles = "I"*age_str
leap_year = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
if (leap_year):
   cake = f'''
             __{candles}_____
             |:H:a:p:p:y:|
             |           |
          ___|___________|___
         |^^^^^^^^^^^^^^^^^^|
         |::B:I:r:t:h:d:a:y:|
         |                  |
         ~~~~~~~~~~~~~~~~~~~~
   '''
   print(cake*2)
else:
   cake = f'''
             __{candles}_____
             |:H:a:p:p:y:|
             |           |
          ___|___________|___
         |^^^^^^^^^^^^^^^^^^|
         |::B:I:r:t:h:d:a:y:|
         |                  |
         ~~~~~~~~~~~~~~~~~~~~
   '''
   print(cake)
