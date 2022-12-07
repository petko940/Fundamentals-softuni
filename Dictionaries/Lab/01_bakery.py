data = input().split()
bakery = dict()

for i in range(0, len(data), 2):
    key = data[i]
    value = int(data[i + 1])
    bakery[key] = value

print(bakery)
