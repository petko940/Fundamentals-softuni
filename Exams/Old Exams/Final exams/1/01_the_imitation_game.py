def move(operations, encrypted_message):
    operations = int(operations[0])
    encrypted_message = encrypted_message[operations:] + encrypted_message[:operations]
    return encrypted_message


def insert(operations, encrypted_message):
    index, value = int(operations[0]), operations[1]
    encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    return encrypted_message


def change_all(operations, encrypted_message):
    substring, replacement = [x for x in operations]
    encrypted_message = encrypted_message.replace(substring, replacement)
    return encrypted_message


def output(encrypted_message):
    return f"The decrypted message is: {encrypted_message}"


def main():
    encrypted_message = input()
    while True:
        commands = input()
        if "Decode" in commands:
            break
        command, *operations = commands.split("|")
        if "Move" in commands:
            encrypted_message = move(operations, encrypted_message)
        elif "Insert" in commands:
            encrypted_message = insert(operations, encrypted_message)
        elif "ChangeAll" in commands:
            encrypted_message = change_all(operations, encrypted_message)
    print(output(encrypted_message))


if __name__ == "__main__":
    main()
