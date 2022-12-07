def add(piece, composer, key, information):
    if piece not in information:
        information[piece] = [composer, key]
        print(f"{piece} by {composer} in {key} added to the collection!")
    else:
        print(f"{piece} is already in the collection!")


def remove(piece, information: dict):
    if piece in information:
        del information[piece]
        print(f"Successfully removed {piece}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def change_key(piece, new_key, information):
    if piece in information:
        information[piece][1] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def main():
    information = {}
    number_of_pieces = int(input())
    for _ in range(number_of_pieces):
        piece, composer, key = input().split("|")
        information[piece] = [composer, key]

    while True:
        commands = input()
        if commands == "Stop":
            break
        command, *data = commands.split("|")
        if command == "Add":
            add(*data, information)
        elif command == "Remove":
            remove(*data, information)
        elif command == "ChangeKey":
            change_key(*data, information)

    for key, value in information.items():
        print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")


main()
