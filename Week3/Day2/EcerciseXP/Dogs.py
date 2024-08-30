class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return round(self.weight / self.age * 10)

    #def fight(self, other_dog):
    #    speed_self = self.run_speed()
    #    if (speed_self*self.weight) > (other_dog*self.weight):
    #        return f"{self.name} is Faster"
    #    else:
    #        return f"{other_dog} is Faster"

Pithpul = Dog("Rex", 14, 90)
Chihuahua = Dog("cheli", 4, 20)
Beagle = Dog("Bebe", 5, 50)

#print(Beagle.bark())

#class Pate(Dog):
#    pass

#my_name = Pate("piter", 12, 150)

#print(my_name.bark())
#print(Pithpul.fight(Beagle.run_speed()))
#print(Beagle.fight(Chihuahua.run_speed()))
#print(Chihuahua.fight(Pithpul.run_speed()))
#print(Pithpul.fight(Chihuahua.run_speed()))



