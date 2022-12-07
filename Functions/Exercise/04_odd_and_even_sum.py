def sum_even_odd(number):
    split_number = [int(x) for x in str(number)]
    sum_odd = sum([odd for odd in split_number if odd % 2 != 0])
    sum_even = sum([even for even in split_number if even % 2 == 0])
    return sum_odd, sum_even


number_as_string = input()
sum_odd, sum_even = sum_even_odd(number_as_string)

print(f"Odd sum = {sum_odd}, Even sum = {sum_even}")
