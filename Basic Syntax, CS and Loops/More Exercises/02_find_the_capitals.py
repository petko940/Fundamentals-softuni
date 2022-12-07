from string import ascii_uppercase

string = input()
output = list()

for i in range(len(string)):
    for j in ascii_uppercase:
        if j in string[i]:
            output.append(i)
            break

print(output)
