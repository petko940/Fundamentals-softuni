from math import factorial


def factorial_division(number1, number2):
    a = factorial(number1)
    b = factorial(number2)
    return a / b


first_number = int(input())
second_number = int(input())
print(f"{factorial_division(first_number, second_number):.2f}")
