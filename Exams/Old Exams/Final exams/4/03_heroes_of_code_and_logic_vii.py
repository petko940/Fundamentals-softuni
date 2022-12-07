def main():
    heroes = {}
    number_of_heroes = int(input())
    for _ in range(number_of_heroes):
        hero_name, hp, mp = [int(x) if x.isdigit() else x for x in input().split()]
        heroes[hero_name] = {'hp': hp, 'mp': mp}

    while True:
        command = input()
        if command == "End":
            break

        event, *data = [int(x) if x.isdigit() else x for x in command.split(" - ")]
        if "CastSpell" in event:
            cast_spell(*data, heroes)
        elif "TakeDamage" in event:
            take_damage(*data, heroes)
        elif "Recharge" in event:
            recharge(*data, heroes)
        elif "Heal" in event:
            heal(*data, heroes)

    for key, value in heroes.items():
        print(f"{key}")
        print(f"HP: {value['hp']}")
        print(f"MP: {value['mp']}")


def cast_spell(hero_name, mp_needed, spell_name, heroes: dict):
    if heroes[hero_name]['mp'] >= mp_needed:
        heroes[hero_name]['mp'] -= mp_needed
        print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['mp']} MP!")
    else:
        print(f"{hero_name} does not have enough MP to cast {spell_name}!")


def take_damage(hero_name, damage, attacker, heroes: dict):
    heroes[hero_name]['hp'] -= damage
    if heroes[hero_name]['hp'] > 0:
        print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['hp']} HP left!")
    else:
        del heroes[hero_name]
        print(f"{hero_name} has been killed by {attacker}!")


def recharge(hero_name, amount, heroes: dict):
    current_mana = heroes[hero_name]['mp']
    heroes[hero_name]['mp'] += amount
    if heroes[hero_name]['mp'] > 200:
        heroes[hero_name]['mp'] = 200
        amount = 200 - current_mana
    print(f"{hero_name} recharged for {amount} MP!")


def heal(hero_name, amount, heroes: dict):
    current_health = heroes[hero_name]['hp']
    heroes[hero_name]['hp'] += amount
    if heroes[hero_name]['hp'] > 100:
        heroes[hero_name]['hp'] = 100
        amount = 100 - current_health
    print(f"{hero_name} healed for {amount} HP!")


main()
