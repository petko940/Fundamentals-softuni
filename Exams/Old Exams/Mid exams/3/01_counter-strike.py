energy = int(input())
command = input()

battles_count = 0
while command != "End of battle":
    distance = int(command)
    if energy >= distance:
        battles_count += 1
        energy -= distance
        if battles_count % 3 == 0:
            energy += battles_count
    elif energy < distance:
        print(f"Not enough energy! Game ends with {battles_count} won battles and {energy} energy")
        break

    command = input()
else:
    print(f"Won battles: {battles_count}. Energy left: {energy}")
