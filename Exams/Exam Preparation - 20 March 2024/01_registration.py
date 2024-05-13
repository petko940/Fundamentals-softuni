username = input()

while True:
    command = input()

    if command == "Registration":
        break

    command = command.split()

    if "Letters" in command:
        username = username.lower() if command[1] == "Lower" else username.upper()
        print(username)

    elif "Reverse" in command:
        start_index, end_index = int(command[1]), int(command[2])
        if 0 <= start_index < len(username) and 0 <= end_index < len(username):
            text = username[start_index:end_index + 1][::-1]
            print(text)

    elif "Substring" in command:
        substring = command[1]
        if substring in username:
            username = username.replace(command[1], "")
            print(username)
        else:
            print(f"The username {username} doesn't contain {substring}.")

    elif "Replace" in command:
        char = command[1]
        username = username.replace(char, "-")
        print(username)

    elif "IsValid" in command:
        char = command[1]
        # if char in username:
        #     print(f"Valid username.")
        # else:
        #     print(f"{char} must be contained in your username.")

        print(f"Valid username.") if char in username else print(f"{char} must be contained in your username.")
