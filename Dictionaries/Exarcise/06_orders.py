def output(data):
    for key, value in data.items():
        total_price = value['price'] * value['quantity']
        print(f"{key} -> {total_price:.2f}")


def main():
    data = {}
    while True:
        info = input()
        if info == "buy":
            break
        name, price, quantity = [x for x in info.split()]
        price, quantity = float(price), int(quantity)
        data[name] = data.get(name, {'price': 0, 'quantity': 0})
        data[name]['price'] = price
        data[name]['quantity'] += quantity

    output(data)


main()

# dictionary = {
#     "name": {},
#     "price": {}
# }
#
# while True:
#     products = input()
#     if products == "buy":
#         break
#
#     name, price, quantity = products.split()
#     quantity = int(quantity)
#     price = float(price)
#     if name not in dictionary["name"]:
#         dictionary["name"][name] = quantity
#         dictionary["price"][name] = price
#     else:
#         dictionary["name"][name] += quantity
#         dictionary["price"][name] = price
#
# for product in dictionary["name"]:
#     current_quantity = dictionary["name"][product]
#     current_price = dictionary["price"][product]
#     total_price = current_quantity * current_price
#     print(f"{product} -> {total_price:.2f}")


# products = input()
# data = {}
# total_quantity = {}
# while "buy" not in products:
#     name, price, quantity = [x for x in products.split()]
#     price = float(price)
#     quantity = int(quantity)
#
#     if name not in data:
#         total_quantity[name] = quantity
#         data[name] = price * total_quantity[name]
#     else:
#         total_quantity[name] += quantity
#         data[name] = price * total_quantity[name]
#     products = input()
#
# [print(f"{name} -> {price:.2f}") for name, price in data.items()]
