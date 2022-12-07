data = {
    "color": {}
}

while True:
    dwarf_data = input()
    if dwarf_data == "Once upon a time":
        break

    name, hat_color, physics = [int(x) if x.isdigit() else x for x in dwarf_data.split(" <:> ")]
    if hat_color not in data["color"]:
        data["color"][hat_color] = {}

    if name not in data["color"][hat_color]:
        data["color"][hat_color][name] = 0

    if data["color"][hat_color][name] < physics:
        data["color"][hat_color][name] = physics

result = []

for hat in data["color"]:
    for name, physics in data["color"][hat].items():
        result.append({"hat_len": len(data["color"][hat]), "name": name, "physics": physics, "color": hat})

for output in sorted(result, key=lambda item: (-item["physics"],-item["hat_len"])):
    print(f"({output['color']}) {output['name']} <-> {output['physics']}")
