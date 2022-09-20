number_order = int(input())

total = 0
for _ in range(number_order):
    price_per_capsule = float(input())
    days = int(input())
    capsules = int(input())
    if not (0.01 <= price_per_capsule <= 100.00 and 1 <= days <= 31 and 1 <= capsules <= 2000):
        continue
    price = price_per_capsule * capsules * days
    print(f"The price for the coffee is: ${price:.2f}")
    total += price

print(f"Total: ${total:.2f}")