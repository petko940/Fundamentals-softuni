phonebook = {}

command = input()
while not command.isnumeric():
    name, number = command.split("-")
    if name not in phonebook:
        phonebook[name] = 0
    phonebook[name] = number
    command = input()

for num in range(int(command)):
    search_contact = input()
    if search_contact not in phonebook:
        print(f"Contact {search_contact} does not exist.")
    else:
        print(f"{search_contact} -> {phonebook[search_contact]}")


# people_and_phone_number = input().split("-")
# phonebook = {}
#
# while people_and_phone_number[0].isalpha():
#     phonebook[people_and_phone_number[0]] = people_and_phone_number[1]
#     people_and_phone_number = input().split("-")
#
# n = int(people_and_phone_number[0])
# for i in range(n):
#     name = input()
#     if name in phonebook.keys():
#         print(f"{name} -> {phonebook.get(name)}")
#     else:
#         print(f"Contact {name} does not exist.")