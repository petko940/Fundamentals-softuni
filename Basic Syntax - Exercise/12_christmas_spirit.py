quantity = int(input())
days_left = int(input())

ornament_set_price = 2
ornament_set_spirit_point = 5
tree_skirt_price = 5
tree_skirt_spirit_point = 3
tree_garland_price = 3
tree_garland_spirit_point = 10
tree_lights_price = 15
tree_lights_spirit_point = 17

price = 0
spirit_point = 0

for i in range(1, days_left + 1):
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        price += quantity * ornament_set_price
        spirit_point += ornament_set_spirit_point
    if i % 3 == 0:
        price += quantity * tree_skirt_price
        price += quantity * tree_garland_price
        spirit_point += tree_skirt_spirit_point + tree_garland_spirit_point
    if i % 5 == 0:
        price += quantity * tree_lights_price
        spirit_point += tree_lights_spirit_point
        if i % 3 == 0 and i % 5 == 0:
            spirit_point += 30
    if i % 10 == 0:
        spirit_point -= 20
        price += tree_skirt_price + tree_garland_price + tree_lights_price

if days_left % 10 == 0:
    spirit_point -= 30

print(f"Total cost: {price}\nTotal spirit: {spirit_point}")
