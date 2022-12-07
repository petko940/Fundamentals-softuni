def rest():
    global total_energy
    current_energy = total_energy
    total_energy += value
    if total_energy >= 100:
        total_energy = 100
    gained_energy = total_energy - current_energy
    print(f"You gained {gained_energy} energy.")
    print(f"Current energy: {total_energy}.")


def order():
    global total_energy, total_coins
    if total_energy - 30 >= 0:
        total_energy -= 30
        total_coins += value
        print(f"You earned {value} coins.")
    else:
        total_energy += 50
        print("You had to rest!")


def any_other_event():
    global total_coins
    if total_coins >= value:
        total_coins -= value
        print(f"You bought {event_type}.")
    else:
        print(f"Closed! Cannot afford {event_type}.")
        quit()


events = [x for x in input().split("|")]
total_energy = 100
total_coins = 100

for current_event in events:
    current_event = current_event.split("-")
    event_type = current_event[0]
    value = int(current_event[1])
    if "rest" in current_event:
        rest()
    elif "order" in current_event:
        order()
    else:
        any_other_event()
else:
    print(f"""Day completed!
Coins: {total_coins}
Energy: {total_energy}
""")
