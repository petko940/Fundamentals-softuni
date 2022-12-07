def register(username, license_plate_number):
    if username in data:
        print(f"ERROR: already registered with plate number {data.get(username)}")
    else:
        data[username] = license_plate_number
        print(f"{username} registered {license_plate_number} successfully")


def unregister(username):
    if data.get(username) is None:
        print(f"ERROR: user {username} not found")
    else:
        data.pop(f"{username}")
        print(f"{username} unregistered successfully")


number_of_commands = int(input())
data = dict()
for current_command in range(number_of_commands):
    command = input()
    if "unregister" in command:
        command = command.split()
        username = command[1]
        unregister(username)
    elif "register" in command:
        username, license_plate_number = [x for x in command.split() if x[0].isupper()]
        register(username, license_plate_number)

[print(f"{username} => {license_plate_number}") for username, license_plate_number in data.items()]
