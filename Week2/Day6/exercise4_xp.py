class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name

    def add_animal(self, new_animal):
        for check_list in range(1):
            if new_animal not in self.zoo_name[0]:
                self.zoo_name[0].append(new_animal)
        #print(f"{self.zoo_name[0]}")
        #print(self.zoo_name[0])
        return self.zoo_name[0]

    def get_animals(self):
        print(self.zoo_name[0])

    def sell_animal(self, animal_sold):
        pass

    def sort_animals(self):
        pass

animals = []
name = "Isreal_Safari"
ramat_gan_safari = Zoo([animals, name])

#ramat_gan_safari.add_animal("Sheip")
#ramat_gan_safari.add_animal("Lion")
#ramat_gan_safari.add_animal("Cat")
#ramat_gan_safari.add_animal("Puma")
#ramat_gan_safari.add_animal("Puma")
#ramat_gan_safari.add_animal("Puma")
#liss = ramat_gan_safari.add_animal("Dog")
#print(liss)

for row in range(4):
    ramat_gan_safari.add_animal(input("Which animal sholus we add to the zoo --> "))

ramat_gan_safari.get_animals()
