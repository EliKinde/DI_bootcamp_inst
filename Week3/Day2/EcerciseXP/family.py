class Family:
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name

    def born(self, **kwargs):
        print("Mazl Tbo to the new born")
        self.members.append(kwargs)

    def is_18(self, name):
        for index in range(len(self.members)):
            if  name in self.members[index].values():
                if self.members[index]["age"] >= 18:
                    return True
                return False


    def family_presentation(self):
        print(f"The last name is {self.last_name}")
        i = 0
        for namea in self.members:
            print(f"My name is: {self.members[i]["name"]} {self.last_name}\nmy age is {self.members[i]["age"]}")
            i += 1

list_of_family = [
                    {'name':'Michael','age':35, 'gender':'Male',   'is_child':False},
                    {'name':'Sarah',  'age':32, 'gender':'Female', 'is_child':False}
                 ]

member_of_family = Family(list_of_family, "Domdov")
#print(member_of_family.last_name)
#print(member_of_family.members[1]["age"])

member_of_family.born(name = 'M.joniur', age = 1, gender = 'Male', is_child = True)
#print(member_of_family.members[2]["name"])

member_of_family.family_presentation()

print(member_of_family.is_18("Sarah"))
print(member_of_family.is_18("Michael"))
print(member_of_family.is_18("M.joniur"))

