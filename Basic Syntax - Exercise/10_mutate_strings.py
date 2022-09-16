first_string, second_string = input(), input()
f1 = [x for x in first_string]
f2 = [x for x in second_string]

for i in range(len(first_string)):
    if f1[i] != f2[i]:
        f1[i] = f2[i]
        print("".join(f1))


# first_string, second_string = input(), input()
#
# for i in range(len(second_string)):
#     if first_string[i] != second_string[i]:
#         old = first_string[i]
#         new = second_string[i]
#         first_string = first_string[:i] + second_string[i:i + 1].replace(old, new, 1) + first_string[i + 1:]
#         print(first_string)
