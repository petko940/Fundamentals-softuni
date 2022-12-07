data = [int(x) for x in input().split("@")]
command = input()
index = 0
count = len(data)
while True:
    command = command.split()
    if "Love!" in command:
        break
    index += int(command[1])
    if index >= len(data):
        index = 0
    if data[index] == 0:
        print(f"Place {index} already had Valentine's day.")
        command = input()
        continue
    data[index] -= 2
    if data[index] == 0:
        print(f"Place {index} has Valentine's day.")
        count -= 1
    command = input()

print(f"Cupid's last position was {index}.")

if all(x == 0 for x in data):
    print("Mission was successful.")
else:
    print(f"Cupid has failed {count} places.")


# even_integers = [int(x) for x in input().split("@")]
# command = input().split()
# index = int(command[1])
# count = len(even_integers)
# while command[0] != "Love!":
#     jump = command[0]
#     if index > len(even_integers) - 1:
#         index = 0
#
#     if even_integers[index] == 0:
#         print(f"Place {index} already had Valentine's day.")
#         command = input().split()
#         if command[0] == "Love!":
#             break
#         index += int(command[1])
#         continue
#
#     even_integers[index] -= 2
#     if even_integers[index] == 0:
#         print(f"Place {index} has Valentine's day.")
#         count -= 1
#     command = input().split()
#
#     if command[0] == "Love!":
#         break
#     index += int(command[1])
#
# print(f"Cupid's last position was {index}.")
# if count == 0:
#     print("Mission was successful.")
# else:
#     print(f"Cupid has failed {count} places.")
