def dragon_fill_dict(type, name, damage, health, armor):
    if type not in dragons_data:
        dragons_data[type] = {}
    if name not in dragons_data[type]:
        dragons_data[type][name] = {}
        dragons_data[type][name]["damage"] = damage
        dragons_data[type][name]["health"] = health
        dragons_data[type][name]["armor"] = armor
    dragons_data[type][name]["damage"] = damage
    dragons_data[type][name]["health"] = health
    dragons_data[type][name]["armor"] = armor


number_of_dragons = int(input())
dragons_data = {}
for _ in range(number_of_dragons):
    # type,name,damage,health,armor = [int(x) if x.isdigit() else x for x in input().split()]
    command = input().split()
    type = command[0]
    name = command[1]

    if command[3] == "null":
        health = 250
    else:
        health = int(command[3])

    if command[2] == "null":
        damage = 45
    else:
        damage = int(command[2])

    if command[-1] == "null":
        armor = 10
    else:
        armor = int(command[-1])

    dragon_fill_dict(type, name, damage, health, armor)

for color, value in dragons_data.items():
    damage_sum = 0
    health_sum = 0
    armor_sum = 0
    count = 0
    for v, k in value.items():
        damage_sum += k["damage"]
        health_sum += k["health"]
        armor_sum += k["armor"]
        count += 1
    print(f"{color}::({damage_sum / count:.2f}/{health_sum / count:.2f}/{armor_sum / count:.2f})")
    for x, y in sorted(dragons_data[color].items()):
        print(f"-{x} -> damage: {dragons_data[color][x]['damage']},"
              f" health: {dragons_data[color][x]['health']},"
              f" armor: {dragons_data[color][x]['armor']}")
