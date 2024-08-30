number = int(input("Enter a Number: "))
length = int(input("Enter a lengt: "))
multipled = []
for num in range(1, length + 1):
    multipled.append(number*num)

print(f"number: {number} - length: {length} --> {multipled}")

