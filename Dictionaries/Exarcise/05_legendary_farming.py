dictionary = {
    "shards": 0,
    "fragments": 0,
    "motes": 0,
}


def legendary_item(material):
    if material == "shards":
        return f"Shadowmourne obtained!"
    elif material == "fragments":
        return f"Valanyr obtained!"
    elif material == "motes":
        return f"Dragonwrath obtained!"


item_ready = False
while True:
    items = input().split()
    for current_item in range(0, len(items), 2):
        quantity, material = int(items[current_item]), items[current_item + 1].lower()
        if material == "shards":
            dictionary["shards"] += quantity
        elif material == "fragments":
            dictionary["fragments"] += quantity
        elif material == "motes":
            dictionary["motes"] += quantity
        else:
            if material not in dictionary:
                dictionary[material] = 0
            dictionary[material] += quantity
        if material == "shards" or material == "fragments" or material == "motes":
            if dictionary[material] >= 250:
                dictionary[material] -= 250
                item_ready = True
                print(legendary_item(material))
                break
    if item_ready:
        break

for k, v in dictionary.items():
    print(f"{k}: {v}")
