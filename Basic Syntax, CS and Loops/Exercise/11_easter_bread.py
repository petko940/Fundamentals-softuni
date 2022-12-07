budged = float(input())
flour_price = float(input())

eggs_price = 0.75 * flour_price
milk_price = (1.25 * flour_price) / 4

loaf_price = eggs_price + flour_price + milk_price

eggs_count = 0
bread_count = 0

while loaf_price < budged:
    eggs_count += 3
    bread_count += 1
    if bread_count % 3 == 0:
        eggs_count -= bread_count - 2
    budged -= loaf_price

print(f"You made {bread_count} loaves of Easter bread! Now you have {eggs_count} eggs and {budged:.2f}BGN left.")
