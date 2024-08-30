my_list = [2,3,4,5,"four",414,334,77,"imanumber"]

total = 0

for number in my_list:
    if type(number) == int(number):
        total += number
    else:
        continue

print(total)
