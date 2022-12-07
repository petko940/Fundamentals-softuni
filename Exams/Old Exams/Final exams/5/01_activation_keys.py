def contains(substring):
    if substring in activation_key:
        print(f"{activation_key} contains {substring}")
    else:
        print("Substring not found!")


def flip(low_up, start_index, end_index, activation_key):
    substring = activation_key[start_index:end_index]
    if low_up == "Upper":
        substring = substring.upper()
    elif low_up == "Lower":
        substring = substring.lower()
    activation_key = activation_key[:start_index] + substring + activation_key[end_index:]
    print(activation_key)
    return activation_key


def slice_function(start_index, end_index, activation_key):
    activation_key = activation_key[:start_index] + activation_key[end_index:]
    print(activation_key)
    return activation_key


def main():
    global activation_key
    while True:
        commands = input()
        if "Generate" in commands:
            break

        commands = commands.split(">>>")
        if "Contains" in commands:
            substring = commands[1]
            contains(substring)
        elif "Flip" in commands:
            command, low_up, start_index, end_index = [int(x) if x.isdigit() else x for x in commands]
            activation_key = flip(low_up, start_index, end_index, activation_key)
        elif "Slice" in commands:
            command, start_index, end_index = [int(x) if x.isdigit() else x for x in commands]
            activation_key = slice_function(start_index, end_index)

    print(f"Your activation key is: {activation_key}")


activation_key = input()
main()
