version = str(int("".join(input().split("."))) + 1)

print(f"{version[0]}.{version[1]}.{version[2]}")


# version = input().split(".")
#
# n1 = int(version[0])
# n2 = int(version[1])
# n3 = int(version[2])
#
# if n3 < 9:
#     n3 += 1
# else:
#     if n2 < 9:
#         n3 = 0
#         n2 += 1
#     else:
#         n3 = 0
#         n2 = 0
#         n1 += 1
#
# print(f"{n1}.{n2}.{n3}")
