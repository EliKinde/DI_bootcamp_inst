class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2}!")


davids_dog = Dog("Rex", 50)
print(f"The dog name is {davids_dog.name} and is heigth {davids_dog.height}")
davids_dog.bark()
davids_dog.jump()

print("")

sarahs_dog = Dog("Teacup", 20)
sarahs_dog.bark()
sarahs_dog.jump()
print(f"The dog name is {sarahs_dog.name} and is heigth {sarahs_dog.height}")

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is the bigger dog")
else:
    print(f"{sarahs_dog.name} is the bigger dog")

