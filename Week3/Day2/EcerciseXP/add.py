#def add(x, y):
#    return x + y

#print("Hellos")
#def sub(x, y):
#    return x - y

print("Impoerted my_module...")

test = "Test String"

def find_index(to_search, target):
    '''Find the index of a value in a swquensce'''

    for i, value in enumerate(to_search):
        if value == target:
            return i
    return -1

