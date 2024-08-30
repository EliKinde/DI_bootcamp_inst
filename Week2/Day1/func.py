def calculation(a, b):
    c = a + b
    if a > b:
        d = a - b
    else:
        d = b -a
    return c ,d

print(calculation(40, 10))
print(calculation(10, 80))

people = ["Rick", "Morty", "Beth", "Jerry", "Snomball"]

def hello(s):
    if s <= 4:
        print("Hello to you")

grtting = map(hello, people)
print(grtting)


