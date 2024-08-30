import string
from random import randint

list_of_char = list(string.ascii_letters)
string_random = []
for i in range(5):
    index = randint(0,53)
    string_random.append(list_of_char[index])

string_random = "".join(string_random)
print(string_random)
