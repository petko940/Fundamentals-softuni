def shoot_target(index, list_):
    removed_element = list_[index]
    list_[index] = -1
    for current_shoot in range(len(list_)):
        if list_[current_shoot] == -1:
            continue
        elif list_[current_shoot] > removed_element:
            list_[current_shoot] -= removed_element
        else:
            list_[current_shoot] += removed_element


data = [int(x) for x in input().split()]
command = input()
count = 0
while "End" not in command:
    command = int(command)
    if 0 <= command < len(data):
        shoot_target(command, data)
        count += 1
    command = input()

print(f"Shot targets: {count} ->", end=" ")
print(*data)


# integers = [int(x) for x in input().split()]
#
# command = input()
# count = 0
# while command not in "End":
#     command = int(command)
#     if 0 <= command < len(integers):
#         current_number = integers[command]
#         count += 1
#         for i in range(len(integers)):
#             if integers[i] > current_number and integers[i] != -1:
#                 integers[i] -= current_number
#             elif integers[i] <= current_number and integers[i] != -1:
#                 integers[i] += current_number
#         integers[command] = -1
#     command = input()
#
# print(f"Shot targets: {count} ->", end=" ")
# print(*integers)
