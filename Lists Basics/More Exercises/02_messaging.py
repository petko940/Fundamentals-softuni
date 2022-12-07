numbers = input().split()
string = input()
output = []

for i in numbers:
    sum_of_digits = 0
    for digits in i:
        sum_of_digits += int(digits)

    sum_of_digits %= len(string)
    output.append(string[sum_of_digits])
    string = string.replace(string[sum_of_digits], "", 1)

print("".join(output))
