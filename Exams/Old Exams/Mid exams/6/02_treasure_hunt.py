def loot(loot_list, items):
    for current_item in items:
        if current_item in loot_list:
            continue
        start_loot.insert(0, current_item)


def drop(loot_list, index):
    index = int(index)
    if 0 <= index < len(start_loot):
        loot_list.append(loot_list.pop(index))


def steal(loot_list, count):
    count = int(count)
    output = loot_list[-count:]
    loot_list = loot_list[:-count]
    print(", ".join(output))
    return loot_list


start_loot = input().split("|")
command = input()

while command not in "Yohoho!":
    command = command.split()
    if "Loot" in command:
        loot(start_loot, command[1:])
    elif "Drop" in command:
        drop(start_loot, command[1])
    elif "Steal":
        start_loot = steal(start_loot, command[1])

    command = input()

average = 0
for item in start_loot:
    average += len(item)

if average > 0:
    average /= len(start_loot)
    print(f"Average treasure gain: {average:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
