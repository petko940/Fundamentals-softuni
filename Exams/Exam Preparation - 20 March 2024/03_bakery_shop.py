foods = {}
all_sold = 0

while True:
    command = input()

    if command == "Complete":
        break

    cmd, quantity, food = [int(x) if x.isdigit() else x for x in command.split()]
    if "Receive" in cmd:
        if quantity > 0:
            foods[food] = foods.get(food, 0) + quantity

    else:
        if food in foods:
            if foods[food] < quantity:
                sold_quantity = foods[food]
                all_sold += sold_quantity
                del foods[food]
                print(f"There aren't enough {food}. You sold the last {sold_quantity} of them.")
            else:
                all_sold += quantity
                foods[food] -= quantity
                print(f"You sold {quantity} {food}.")
                if foods[food] == 0:
                    foods.pop(food)
        else:
            print(f"You do not have any {food}.")

# for key, value in foods.items():
#     print(f"{key}: {value}")

[print(f"{key}: {value}") for key, value in foods.items()]

print(f"All sold: {all_sold} goods")
