# n = int(input())
#
# for i in range(1, n + 1):
#     digits = i
#     sum_digits = 0
#     while digits > 0:
#         sum_digits += digits % 10
#         digits //= 10
#
#     if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
#         print(f"{i} -> True")
#     else:
#         print(f"{i} -> False")
#

n = int(input())

for i in range(1, n + 1):
    digits = i
    sum_digits = 0
    is_special = False
    while digits > 0:
        sum_digits += digits % 10
        digits //= 10

    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        is_special = True

    print(f"{i} -> {is_special}")
