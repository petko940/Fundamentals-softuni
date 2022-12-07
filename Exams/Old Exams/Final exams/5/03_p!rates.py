def main():
    information = {
        'city': {}
    }
    while True:
        info = input()
        if "Sail" in info:
            break

        city, population, gold = [int(x) if x.isdigit() else x for x in info.split("||")]
        # if city not in information['city']:
        #     information['city'][city] = {'population': 0, 'gold': 0}
        information['city'][city] = information['city'].get(city, {'population': 0, 'gold': 0})
        information['city'][city]['population'] += population
        information['city'][city]['gold'] += gold

    while True:
        commands = input()
        if commands == "End":
            break
        event, *data = [int(x) if x.isdigit() else x for x in commands.split("=>")]
        if event == "Plunder":
            plunder(*data, information)
        elif event == "Prosper":
            prosper(*data, information)

    output(information)


def plunder(town, people, gold, information):
    print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
    information['city'][town]['population'] -= people
    information['city'][town]['gold'] -= gold
    if information['city'][town]['population'] <= 0 or information['city'][town]['gold'] <= 0:
        del information['city'][town]
        print(f"{town} has been wiped off the map!")


def prosper(town, gold, information):
    if int(gold) < 0:
        print("Gold added cannot be a negative number!")
        return information
    else:
        information['city'][town]['gold'] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {information['city'][town]['gold']} gold.")


def output(information):
    if len(information['city']):
        print(f"Ahoy, Captain! There are {len(information['city'])} wealthy settlements to go to:")
        for key, value in information['city'].items():
            print(f"{key} -> Population: {value['population']} citizens, Gold: {value['gold']} kg")
    else:
        print("Ahoy, Captain! All targets have been plundered and destroyed!")


main()

# def main():
#     cities_info = {}
#     while True:
#         command = input()
#         if command == "Sail":
#             break
#         city, population, gold = [int(x) if x.isdigit() else x for x in command.split("||")]
#         if city not in cities_info:
#             cities_info[city] = [population, gold]
#         else:
#             cities_info[city][0] += population
#             cities_info[city][1] += gold
#
#     while True:
#         commands = input()
#         if commands == "End":
#             break
#         if "Plunder" in commands:
#             event, town, people, gold = [int(x) if x.isdigit() else x for x in commands.split("=>")]
#             plunder(town, people, gold, cities_info)
#         elif "Prosper" in commands:
#             event, town, gold = [int(x) if x.isdigit() else x for x in commands.split("=>")]
#             prosper(town, gold, cities_info)
#
#     output(cities_info)
#
#
# def plunder(town, people, gold, cities_info):
#     cities_info[town][0] -= people
#     cities_info[town][1] -= gold
#     print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
#     if cities_info[town][0] <= 0 or cities_info[town][1] <= 0:
#         cities_info.pop(town)
#         print(f"{town} has been wiped off the map!")
#
#
# def prosper(town, gold, cities_info):
#     gold = int(gold)
#     if gold < 0:
#         print("Gold added cannot be a negative number!")
#     else:
#         cities_info[town][1] += gold
#         print(f"{gold} gold added to the city treasury. {town} now has {cities_info[town][1]} gold.")
#
#
# def output(cities_info):
#     if len(cities_info) > 0:
#         print(f"Ahoy, Captain! There are {len(cities_info)} wealthy settlements to go to:")
#         for key, value in cities_info.items():
#             print(f"{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg")
#     else:
#         print("Ahoy, Captain! All targets have been plundered and destroyed!")
#
#
# main()
