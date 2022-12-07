def sum_number(a, b):
    return a + b


def subtract(ab, c):
    return ab - c


def add_and_subtract(a, b, c):
    return subtract(sum_number(a, b), c)


num1 = int(input())
num2 = int(input())
num3 = int(input())
print(add_and_subtract(num1, num2, num3))
