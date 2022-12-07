def shoot(index_def, power, list_: list):
    if 0 <= index_def < len(list_):
        list_[index_def] -= power
        if list_[index_def] <= 0:
            list_.remove(list_[index_def])


def add(index_def, value, list_: list):
    if 0 <= index_def < len(list_):
        list_.insert(index_def, value)
    else:
        print("Invalid placement!")


def strike(index_def, radius, list_: list):
    whole_radius = 2 * radius + 1
    if 0 <= index_def - radius < len(list_) and 0 <= index_def + radius < len(list_):
        for i in range(whole_radius):
            list_.remove(list_[index_def - radius])
    else:
        print("Strike missed!")


targets = [int(x) for x in input().split()]
command = input()
while "End" not in command:
    command = command.split()
    index, event = int(command[1]), int(command[2])
    if "Shoot" in command:
        shoot(index, event, targets)
    elif "Add" in command:
        add(index, event, targets)
    elif "Strike" in command:
        strike(index, event, targets)
    command = input()

print(*targets, sep="|")
