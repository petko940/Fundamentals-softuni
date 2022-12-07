def straight(force_side, force_user, data):
    flag = False
    for value in data.values():
        if force_user in value:
            flag = True
            break
    if not flag:
        if force_side not in data.keys():
            data[force_side] = [force_user]
        else:
            data[force_side].append(force_user)


def arrow(force_user, force_side, data):
    for key, value in data.items():
        if force_user in value:
            data[key].remove(force_user)
            break
    if force_side not in data.keys():
        data[force_side] = [force_user]
    else:
        data[force_side].append(force_user)


data = {}
command = input()
while command != "Lumpawaroo":
    if "|" in command:
        force_side, force_user = command.split(" | ")
        straight(force_side, force_user, data)
    elif "->" in command:  # else
        force_user, force_side = command.split(" -> ")
        arrow(force_user, force_side, data)
        print(f"{force_user} joins the {force_side} side!")
    command = input()

for key, value in data.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        for user in value:
            print(f"! {user}")
