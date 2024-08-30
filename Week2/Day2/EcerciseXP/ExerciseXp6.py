magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(names):
    for name in names:
        print(name)

show_magicians(magician_names)

def make_great(names):
    great = "the Great "
    magici = []
    for name in range(len(names)):
        names[name] = great + names[name]

make_great(magician_names)

show_magicians(magician_names)

