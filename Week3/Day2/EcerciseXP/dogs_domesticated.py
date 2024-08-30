from Dogs import Dog

class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        Dog.__init__(self, name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        i = 0
        for dog_name in args:
            print(f"{dog_name} all play together")

    def do_a_trick():
        pass

rxi = PetDog("Rxi", 5, 50)
bella = PetDog("Bella",1, 32)
cj = PetDog("Cj",6, 72)
jake = PetDog("Jake",4, 42)
lexi = PetDog("Lexi",2, 66)

# print the Output of bark methoed
cj.train()

# Print stirng of *args instances

dog_one = bella.name
dog_two = cj.name
dog_three = jake.name
dog_four = lexi.name

rxi.play(dog_one, dog_two, dog_three, dog_four)
