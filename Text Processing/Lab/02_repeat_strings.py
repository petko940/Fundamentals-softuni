strings = input().split()
output = []
for x in range(len(strings)):
    output.append(strings[x] * len(strings[x]))

print("".join(output))
