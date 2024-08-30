class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

    def name_age(self):
        cat_info = [self.name, self.age]
        return cat_info

cat_white = Cat("windy", 1222)
cat_black = Cat("max", 5)
cat_browen = Cat("jj", 60)


def oldest_cat(age_one, age_two, age_three):
    list_age = [age_one, age_two, age_three]
    list_cat_info = [cat_white.name_age(),cat_black.name_age(),cat_browen.name_age()]
    #print(list_cat_info)
    oldest_cat_one = max(list_age)

    age_name_cat = []
    for row in list_cat_info:
        for k in row:
            if k == oldest_cat_one:
                age_name_cat = row
                break
    print(f"Thr oldest cat is {age_name_cat[0]}, and is {age_name_cat[1]} years old")
    return oldest_cat_one

olde = oldest_cat(cat_white.age, cat_black.age, cat_browen.age)
