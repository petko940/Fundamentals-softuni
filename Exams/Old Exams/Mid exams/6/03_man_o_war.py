def fire(number, damage, warship_list):
    if 0 <= number < len(warship_list):
        warship_list[number] -= damage
        if warship_list[number] <= 0:
            print("You won! The enemy ship has sunken.")
            exit()


def defend(start_number, end_number, damage, pirate_ship_list):
    if 0 <= start_number < len(pirate_ship_list) and 0 <= end_number < len(pirate_ship_list):
        for current_section in range(start_number, end_number + 1):
            pirate_ship_list[current_section] -= damage
            if pirate_ship_list[current_section] <= 0:
                print("You lost! The pirate ship has sunken.")
                exit()


def repair(number, health, max_hp, pirate_ship_list):
    if 0 <= number < len(pirate_ship_list):
        pirate_ship_list[number] += health
        if pirate_ship_list[number] > max_hp:
            pirate_ship_list[number] = max_hp


def status(pirate_ship_list, max_hp):
    count = 0
    for current_section in pirate_ship_list:
        if current_section < 0.2 * max_hp:
            count += 1
    return f"{count} sections need repair."


pirate_ship_status = [int(x) for x in input().split(">")]
warship_status = [int(x) for x in input().split(">")]
maximum_health = int(input())

commands = input()
while "Retire" not in commands:
    commands = commands.split()
    command = commands[0]
    if "Fire" in command:
        index = int(commands[1])
        dmg = int(commands[2])
        fire(index, dmg, warship_status)
    elif "Defend" in command:
        start_index = int(commands[1])
        end_index = int(commands[2])
        dmg = int(commands[3])
        defend(start_index, end_index, dmg, pirate_ship_status)
    elif "Repair" in command:
        index = int(commands[1])
        hp = int(commands[2])
        repair(index, hp, maximum_health, pirate_ship_status)
    elif "Status" in command:
        print(status(pirate_ship_status, maximum_health))

    commands = input()

sum_pirates = sum(pirate_ship_status)
sum_warship = sum(warship_status)

print(f"""Pirate ship status: {sum_pirates}
Warship status: {sum_warship}""")
