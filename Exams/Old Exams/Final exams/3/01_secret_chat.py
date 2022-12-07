def insert_space(data, message):
    index = int(data[0])
    message = message[:index] + " " + message[index:]
    return message


def reverse(data, message):
    substring = data[0][::-1]
    if data[0] in message:
        message = message.replace(data[0], "", 1)
        message = message + substring
        print(message)
    else:
        print("error")
    return message


def change_all(data, message):
    substring, replacement = [x for x in data]
    message = message.replace(substring, replacement)
    return message


def main():
    message = input()
    command = input()
    while "Reveal" not in command:
        com, *data = command.split(":|:")
        if "InsertSpace" in com:
            message = insert_space(data, message)
            print(message)
        elif "Reverse" in com:
            message = reverse(data, message)
        elif "ChangeAll" in com:
            message = change_all(data, message)
            print(message)
        command = input()
    print(f"You have a new text message: {message}")


if __name__ == "__main__":
    main()
