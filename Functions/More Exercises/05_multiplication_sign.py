# Try to do this WITHOUT multiplying the 3 numbers.

def multiplication_sign(num1, num2, num3):
    if num1 == 0 or num2 == 0 or num3 == 0:
        return "zero"
    lst = [num1, num2, num3]
    positive_count, negative_count = 0, 0
    for current_number in lst:
        if current_number > 0:
            positive_count += 1
        else:
            negative_count += 1
    if negative_count == 1 or negative_count == 3:
        return "negative"
    return "positive"


number1 = int(input())
number2 = int(input())
number3 = int(input())
print(multiplication_sign(number1, number2, number3))
