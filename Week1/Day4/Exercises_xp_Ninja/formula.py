import math

D = input("Enter a numbers in comma separetd: ")
D = D.split(",")
print(D)
C = 50
H = 30
Q = []

for num in D:
    Q.append(int(math.sqrt((2*C*int(num)/H))))

print(Q)


