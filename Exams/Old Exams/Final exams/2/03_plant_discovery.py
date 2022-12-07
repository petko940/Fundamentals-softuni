def rate(plant, rating, plants_information):
    if plant not in plants_information:
        print("error")
    else:
        plants_information[plant]['rating'].append(rating)


def update(plant, new_rarity, plants_information):
    if plant not in plants_information:
        print("error")
    else:
        plants_information[plant]['rarity'] = new_rarity


def reset(plant, plants_information):
    if plant not in plants_information:
        print("error")
    else:
        plants_information[plant]['rating'].clear()


def output(plant_information):
    print("Plants for the exhibition:")
    for key, value in plant_information.items():
        if len(value['rating']) == 0:
            average = 0
        else:
            average = sum(value['rating']) / len(value['rating'])
        print(f"- {key}; Rarity: {value['rarity']}; Rating: {average:.2f}")


def main():
    plants_information = {}
    n = int(input())
    for _ in range(n):
        plant, rarity = [int(x) if x.isdigit() else x for x in input().split("<->")]
        plants_information[plant] = plants_information.get(plant, {'rarity': 0, 'rating': []})
        plants_information[plant]['rarity'] = rarity

    while True:
        command = input().split(": ")
        if "Exhibition" in command:
            break
        if "Rate" in command:
            plant, rating = [int(x) if x.isdigit() else x for x in command[1].split(" - ")]
            rate(plant, rating, plants_information)
        elif "Update" in command:
            plant, new_rarity = [int(x) if x.isdigit() else x for x in command[1].split(" - ")]
            update(plant, new_rarity, plants_information)
        elif "Reset" in command:
            plant = command[1]
            reset(plant, plants_information)

    output(plants_information)


main()

# from statistics import mean
#
#
# def error():
#     print("error")
#
#
# def rate(plant, data, information):
#     if plant not in information:
#         error()
#     else:
#         information[plant]["rate"].append(data)
#     return information
#
#
# def update(plant, data, information):
#     if plant not in information:
#         error()
#     else:
#         information[plant]["rarity"] = data
#     return information
#
#
# def reset(plant, information):
#     if plant not in information:
#         error()
#     else:
#         information[plant]["rate"].clear()
#     return information
#
#
# def print_data(information):
#     print("Plants for the exhibition:")
#     for key, value in information.items():
#         if len(value["rate"]):
#             print(f"- {key}; Rarity: {value['rarity']}; Rating: {mean(value['rate']):.2f}")
#         else:
#             print(f"- {key}; Rarity: {value['rarity']}; Rating: 0.00")
#
#
# def main():
#     information = {}
#     number = int(input())
#     for _ in range(number):
#         plant, rarity = [int(x) if x.isdigit() else x for x in input().split("<->")]
#         information[plant] = {"rarity": rarity, "rate": []}
#
#     while True:
#         commands = input()
#         if commands == "Exhibition":
#             break
#         commands = commands.replace(":", " -")
#         commands = commands.split(" - ")
#         if "Rate" in commands:
#             current_plant, rating = commands[1], int(commands[2])
#             information = rate(current_plant, rating, information)
#         elif "Update" in commands:
#             current_plant, new_raring = commands[1], int(commands[2])
#             information = update(current_plant, new_raring, information)
#         elif "Reset" in commands:
#             current_plant = commands[1]
#             information = reset(current_plant, information)
#     print_data(information)
#
#
# main()
