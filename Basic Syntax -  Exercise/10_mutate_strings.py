# first_string, second_string = input(), input()
# f1 = [x for x in first_string]
# f2 = [x for x in second_string]
#
# for i in range(len(first_string)):
#     if f1[i] != f2[i]:
#         f1[i] = f2[i]
#         print("".join(f1))


first_string, second_string = input(), input()

for i in range(len(second_string)):
    left = second_string[:i + 1]
    right = first_string[i + 1:]
    if first_string[i] == second_string[i]:
        continue
    print(left + right)

