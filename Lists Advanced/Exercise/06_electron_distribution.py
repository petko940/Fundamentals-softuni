number_of_electrons = int(input())
n = number_of_electrons
# 1 = 2 * 1 ** 2   2 = 2 * 2 ** 2    3 = 2 * 3 ** 2
shell = 1
while n > 0:
    n = n - 2 * shell ** 2
    shell += 1

number_shells = [0] * (shell - 1)

while number_of_electrons > 0:
    for i in range(1, len(number_shells) + 1):
        num = 2 * i ** 2
        if num > number_of_electrons:
            num = number_of_electrons
        number_shells.pop(i - 1)
        number_shells.insert(i - 1, num)
        number_of_electrons -= num

print(number_shells)
