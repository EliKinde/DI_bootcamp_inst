sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich",
                   "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
i = 0
while i < len(sandwich_orders):
    if sandwich_orders[i] == "Pastrami sandwich":
        sandwich_orders.remove("Pastrami sandwich")
    i += 1



finished_sandwiches = []
for k in range(len(sandwich_orders)):
    finished = sandwich_orders[k]
    finished_sandwiches.append(finished)

sandwich_orders.clear()

for item in range(len(finished_sandwiches)):
    print(f"I made your {finished_sandwiches[item].casefold()}")

