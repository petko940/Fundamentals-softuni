def take_odd(password):
    password = [password[x] for x in range(len(password)) if x % 2 != 0]
    print("".join(password))
    return "".join(password)


def cut(index, length, password):
    password = password[:index] + password[index + length:]
    print(password)
    return password


def substitute(substring, substitute, password):
    if substring in password:
        password = password.replace(substring, substitute)
        print(password)
    else:
        print("Nothing to replace!")
    return password


def main():
    password = input()

    while True:
        commands = input()
        if commands == "Done":
            break

        command, *data = [int(x) if x.isdigit() else x for x in commands.split()]
        if command == "TakeOdd":
            password = take_odd(password)
        elif command == "Cut":
            password = cut(*data, password)
        elif command == "Substitute":
            password = substitute(*data, password)

    print(f"Your password is: {password}")


if __name__ == "__main__":
    main()
