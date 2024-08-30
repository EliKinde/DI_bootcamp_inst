number = int(input("Enter a number: "))
length = int(input("Enter a length: "))

multi = 1

for i in range(length):
    i = multi * number
   # print(f"number: {number}, length {length}")
    print(i)
    multi += 1


