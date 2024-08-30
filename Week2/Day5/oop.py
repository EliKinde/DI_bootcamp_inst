class Dog():
    def _init_(self, name_dog):
        print("you created a dog")
        print("His name is", name_dog)
        self.name_dog = name_dog

    def bark(self):
        print(f"{slef.name_dog} bark ")

    def walk(self, num_meters):
        print(f"{self.name_dog} walked {num_meters} meters")


gg = Dog("Rek")
gg.walk(10)


class Robot():
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def intoduceSelf(self):
        print(f"my name is {self.name}, and color {self.color}, {self.weight}")

r1 = Robot("Tom", "red", 30)


r1.intoduceSelf()
