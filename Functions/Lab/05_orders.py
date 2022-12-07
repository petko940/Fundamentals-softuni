def total_price(order, quantity):
    price = None
    if order == "coffee":
        price = 1.5 * quantity
    elif order == "water":
        price = 1 * quantity
    elif order == "coke":
        price = 1.4 * quantity
    elif order == "snacks":
        price = 2 * quantity
    return price


string = input()
number = int(input())
print(f"{total_price(string, number):.2f}")
