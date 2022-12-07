import re

regex = r"^[A-Za-z0-9_]*$"


def make_upper(index, password):
    upper = password[index].upper()
    password = password[:index] + upper + password[index + 1:]
    print(password)
    return password


def make_lower(index, password):
    lower = password[index].lower()
    password = password[:index] + lower + password[index + 1:]
    print(password)
    return password


def insert(index, char, password):
    if 0 <= index <= len(password):
        password = password[:index] + char + password[index:]
        print(password)
    return password


def replace(char, value, password):
    if char in password:
        updated_char = ord(char)
        new_char = chr(updated_char + value)
        password = password.replace(char, new_char)
        print(password)
    return password


def validation(password):
    if len(password) < 8:
        print("Password must be at least 8 characters long!")
    if not re.match(regex, password):
        print("Password must consist only of letters, digits and _!")
    if not any(x.isupper() for x in password):
        print("Password must consist at least one uppercase letter!")
    if not any(x.islower() for x in password):
        print("Password must consist at least one lowercase letter!")
    if not any(x.isdigit() for x in password):
        print("Password must consist at least one digit!")
    return password


def main():
    password = input()
    while True:
        commands = input()
        if "Complete" in commands:
            break
        commands = commands.split()
        event = commands[0]
        if "Make" in event:
            upper_lower = commands[1]
            index = int(commands[2])
            if upper_lower == "Upper":
                password = make_upper(index, password)
            else:
                password = make_lower(index, password)
        elif event == "Insert":
            index, char = int(commands[1]), commands[2]
            password = insert(index, char, password)
        elif event == "Replace":
            char, value = commands[1], int(commands[2])
            password = replace(char, value, password)
        elif event == "Validation":
            password = validation(password)


main()

# import re
#
# regex = r"^[A-Za-z0-9_]*$"
#
# password = input()
#
# while True:
#     commands = input()
#     if "Complete" in commands:
#         break
#
#     if "Make Upper" in commands:
#         index = [int(x) for x in commands.split() if x.isdigit()]
#         index = index[0]
#         upper = password[index].upper()
#         password = password[:index] + upper + password[index + 1:]
#         print(password)
#     elif "Make Lower" in commands:
#         index = [int(x) for x in commands.split() if x.isdigit()]
#         index = index[0]
#         lower = password[index].lower()
#         password = password[:index] + lower + password[index + 1:]
#         print(password)
#     elif "Insert" in commands:
#         commands = commands.split()
#         index, char = int(commands[1]), commands[2]
#         if 0 <= index < len(password):
#             password = password[:index] + char + password[index:]
#             print(password)
#     elif "Replace" in commands:
#         commands = commands.split()
#         char, value = commands[1], int(commands[2])
#         num_char = ord(char)
#         new_char = chr(num_char + value)
#         password = password.replace(char, new_char)
#         print(password)
#     elif "Validation" in commands:
#         if len(password) < 8:
#             print("Password must be at least 8 characters long!")
#         if not re.match(regex, password):
#             print("Password must consist only of letters, digits and _!")
#         if not any(x.isupper() for x in password):
#             print("Password must consist at least one uppercase letter!")
#         if not any(x.islower() for x in password):
#             print("Password must consist at least one lowercase letter!")
#         if not any(x.isdigit() for x in password):
#             print("Password must consist at least one digit!")
