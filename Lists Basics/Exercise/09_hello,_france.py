def function():
    global budget, profit
    if item == "Clothes" and price <= 50 or \
            item == "Shoes" and price <= 35 or \
            item == "Accessories" and price <= 20.5:
        budget -= price
        print(f"{price * 1.4:.2f}", end=" ")
        profit += price * 1.4 - price
        new_price.append(price * 1.4)


items_and_price = [x for x in input().split("|")]
budget = float(input())
new_price = []
profit = 0

for i in range(len(items_and_price)):
    items_and_price_split = items_and_price[i].split("->")
    item = items_and_price_split[0]
    price = float(items_and_price_split[1])
    if budget >= price:
        function()

print(f"\nProfit: {profit:.2f}")
if sum(new_price) + budget > 150:
    print("Hello, France!")
else:
    print("Not enough money.")
