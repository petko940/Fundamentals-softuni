def min_max_sum(array):
    sorted_array = sorted(array)
    min_number = sorted_array[0]
    max_number = sorted_array[-1]
    sum_number = sum(array)
    print(f"""The minimum number is {min_number}
The maximum number is {max_number}
The sum number is: {sum_number}""")


numbers = [int(x) for x in input().split()]
min_max_sum(numbers)
