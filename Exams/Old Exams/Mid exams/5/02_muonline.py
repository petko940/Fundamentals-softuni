def potion(event):
    global health
    health += event
    if health > 100:
        healed = abs(event - health + 100)
        health = 100
        print(f"You healed for {healed} hp.")
    else:
        print(f"You healed for {event} hp.")
    print(f"Current health: {health} hp.")


def chest(num):
    global bitcoins
    bitcoins += num
    return f"You found {num} bitcoins."


def monster(monster_name, attack):
    global health
    health -= attack
    if health > 0:
        return f"You slayed {monster_name}."
    else:
        return f"You died! Killed by {monster_name}."


health = 100
bitcoins = 0
dungeons_rooms = input().split("|")
count_rooms = 0
for current_room in dungeons_rooms:
    count_rooms += 1
    command, number = current_room.split()
    number = int(number)
    if "potion" in command:
        potion(number)
    elif "chest" in command:
        print(chest(number))
    else:
        print(monster(command, number))
        if health <= 0:
            print(f"Best room: {count_rooms}")
            break
else:
    print(f"""You've made it!
Bitcoins: {bitcoins}
Health: {health}""")

