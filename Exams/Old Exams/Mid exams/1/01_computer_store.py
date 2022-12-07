price = input()

total_price = 0
while price != "special" and price != "regular":
    price = float(price)
    if price < 0:
        print("Invalid price!")
        price = input()
        continue
    total_price += price
    price = input()

tax = 0.2 * total_price
special = 1
if price == "special":
    special = 0.9

if total_price == 0:
    print("Invalid order!")
else:
    print(f"""Congratulations you've just bought a new computer!
Price without taxes: {total_price:.2f}$
Taxes: {tax:.2f}$
-----------
Total price: {(total_price + tax )* special:.2f}$""")
