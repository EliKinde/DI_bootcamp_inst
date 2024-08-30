sequence = []

for num in range(1, 6):
    if type(num) == type(int()):
        sequence.append(num)
        num += 0.5
        sequence.append(num)
print(sequence)
