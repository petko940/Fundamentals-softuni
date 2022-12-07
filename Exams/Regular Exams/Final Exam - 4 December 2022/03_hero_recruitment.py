def enroll(hero_name, heroes: dict):
    if hero_name in heroes:
        print(f"{hero_name} is already enrolled.")
    else:
        heroes[hero_name] = []


def learn(hero_name, spell_name, heroes: dict):
    if hero_name not in heroes:
        print(f"{hero_name} doesn't exist.")
    else:
        if spell_name in heroes[hero_name]:
            print(f"{hero_name} has already learnt {spell_name}.")
        else:
            heroes[hero_name].append(spell_name)


def unlearn(hero_name, spell_name, heroes: dict):
    if hero_name not in heroes:
        print(f"{hero_name} doesn't exist.")
    else:
        if spell_name not in heroes[hero_name]:
            print(f"{hero_name} doesn't know {spell_name}.")
        else:
            heroes[hero_name].remove(spell_name)


def output(heroes):
    print("Heroes:")
    for key, value in heroes.items():
        print(f"== {key}: {', '.join(value)}")


def main():
    heroes = {}
    while True:
        commands = input()
        if commands == "End":
            break
        event, *data = [x for x in commands.split()]
        if event == "Enroll":
            enroll(*data, heroes)
        elif event == "Learn":
            learn(*data, heroes)
        elif event == "Unlearn":
            unlearn(*data, heroes)

    output(heroes)


main()
