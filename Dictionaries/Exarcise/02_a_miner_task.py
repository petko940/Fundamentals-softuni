dictionary = {}

while True:
    resource = input()
    if resource == "stop":
        break

    quantity = int(input())
    if resource not in dictionary:
        dictionary[resource] = 0
    dictionary[resource] += quantity

for resource, quantity in dictionary.items():
    print(f"{resource} -> {quantity}")
