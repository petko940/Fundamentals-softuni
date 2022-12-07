def perfect_number(number):
    sum_numbers = 0
    for i in range(1,number//2+1):
        if number % i == 0:
            sum_numbers += i
    if number == sum_numbers:
        return "We have a perfect number!"

    return "It's not so perfect."


integer = int(input())
print(perfect_number(integer))
