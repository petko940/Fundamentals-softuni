def collect(item, data_func: list):
    if item not in data_func:
        data_func.append(item)


def drop(item, data_func: list):
    if item in data_func:
        data_func.remove(item)


def combine_items(old_item, new_item, data_func: list):
    if old_item in data_func:
        index = data_func.index(old_item)
        data_func.insert(index + 1, new_item)


def renew(item, data_func: list):
    if item in data_func:
        index = data_func.index(item)
        change_pos = data_func.pop(index)
        data_func.append(change_pos)


data = input().split(", ")
while True:
    command_data = input()

    if "Craft!" in command_data:
        break

    command, product = command_data.split(" - ")
    if "Collect" in command:
        collect(product, data)
    elif "Drop" in command:
        drop(product, data)
    elif "Combine" in command:
        old_product, new_product = product.split(":")
        combine_items(old_product, new_product, data)
    elif "Renew" in command:
        renew(product, data)

print(*data, sep=", ")


# def collect():
#     item = command[1]
#     if item not in inventory:
#         inventory.append(item)
#
#
# def drop():
#     item = command[1]
#     if item in inventory:
#         inventory.remove(item)
#
#
# def combine_items():
#     split = command[1].split(":")
#     old_item = split[0]
#     if old_item not in inventory:
#         return old_item
#     new_item = split[1]
#     old_new_index = inventory.index(old_item)
#     if old_item in inventory:
#         inventory.insert(old_new_index + 1, new_item)
#
#
# def renew():
#     item = command[1]
#     if item in inventory:
#         inventory.append(inventory.pop(inventory.index(item)))
#
#
# inventory = input().split(", ")
# command = input()
#
# while command != "Craft!":
#     command = command.split(" - ")
#     if "Collect" in command:
#         collect()
#     elif "Drop" in command:
#         drop()
#     elif "Combine Items" in command:
#         combine_items()
#     elif "Renew" in command:
#         renew()
#
#     command = input()
#
# print(*inventory, sep=", ")
