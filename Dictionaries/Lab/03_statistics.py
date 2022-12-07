products = {}

total_products = 0
total_quantity = 0
command = input()
while "statistics" not in command:
    product, quantity = [x if x.isdigit() else x for x in command.split(": ")]
    quantity = int(quantity)
    if product not in products:
        products[product] = 0
    products[product] += quantity
    total_quantity += products[product]
    command = input()

print("Products in stock:")
# for (product, quantity) in products.items():
#     print(f"- {product}: {quantity}")
[print(f"- {product}: {quantity}") for product, quantity in products.items()]

print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
