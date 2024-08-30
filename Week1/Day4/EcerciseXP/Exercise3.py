basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")
basket.remove("Blueberries")

basket.append("Kiwi")

apples_num = basket.count("Apples")
print(basket, apples_num)


basket.clear()
print(basket)
