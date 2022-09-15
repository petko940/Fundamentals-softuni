number = int(input())

[print(x * "*") for x in range(1, number + 1)]
[print(x * "*") for x in range(number - 1, 0, -1)]


# for i in range(number):
#     for j in range(i + 1):
#         print("*", end="")
#     print()
#
# for x in range(number - 1, 0, -1):
#     for y in range(number - 1):
#         print("*", end="")
#     number -= 1
#     print()
