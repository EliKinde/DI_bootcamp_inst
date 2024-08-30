"""
total_cost = []
while True:
    age = input("Enter tour ages: ")
    total_cost.append(age)
    if age == "quit":
        total_cost.pop()
        break

print(total_cost)
"""

user_word = list(input("Enter your word: "))
data = []
for word in user_word:
    if word not in data:
        data.append(word)

st = "".join(data)


print(st)
