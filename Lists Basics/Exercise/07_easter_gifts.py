def OutOfStock():
    gift = command[1]
    for i in range(len(names_of_the_gifts)):
        if names_of_the_gifts[i] == gift:
            names_of_the_gifts[i] = "None"


def Required():
    gift = command[1]
    index = int(command[2])
    if 0 <= index < len(names_of_the_gifts):
        names_of_the_gifts[index] = gift


def JustInCase():
    gift = command[1]
    names_of_the_gifts[-1] = gift


names_of_the_gifts = input().split()
command = input()

while "No Money" not in command:
    command = command.split()
    if "OutOfStock" in command:
        OutOfStock()
    elif "Required" in command:
        Required()
    elif "JustInCase" in command:
        JustInCase()
    command = input()

for i in names_of_the_gifts:
    if "None" in names_of_the_gifts:
        names_of_the_gifts.remove("None")
print(*names_of_the_gifts)
