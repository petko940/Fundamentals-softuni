string = input()

for index1, index2 in enumerate(range(len(string) - 1)):
    if string[index1] != string[index2 + 1]:
        print(string[index1], end="")

print(string[-1])
