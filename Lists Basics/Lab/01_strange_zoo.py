zoo = list()

for _ in range(3):
    new_element = input()
    zoo.append(new_element)

zoo[0], zoo[2] = zoo[2], zoo[0]

print(zoo)
