import sys

numbers = [int(x) for x in input().split()]
command = input().split()

while command[0] != "end":
    even_numbers = [even for even in numbers if even % 2 == 0]
    odd_numbers = [odd for odd in numbers if odd % 2 != 0]
    max_value = -sys.maxsize
    min_value = sys.maxsize
    value_index = 0
    is_found = False
    count = 0

    if command[0] == "exchange":
        index = int(command[1])
        if index < 0 or index >= len(numbers):
            print("Invalid index")
        else:
            numbers = numbers[index + 1:] + numbers[:index + 1]

    elif command[0] == "max":
        if command[1] == "even":
            for index, value in enumerate(numbers):
                if value % 2 == 0:
                    if value >= max_value:
                        max_value = value
                        value_index = index
                        is_found = True
        elif command[1] == "odd":
            for index, value in enumerate(numbers):
                if value % 2 != 0:
                    if value >= max_value:
                        max_value = value
                        value_index = index
                        is_found = True
        if is_found:
            print(value_index)
        else:
            print("No matches")

    elif command[0] == "min":
        if command[1] == "even":
            for index, value in enumerate(numbers):
                if value % 2 == 0:
                    if value <= min_value:
                        min_value = value
                        value_index = index
                        is_found = True
        elif command[1] == "odd":
            for index, value in enumerate(numbers):
                if value % 2 != 0:
                    if value <= min_value:
                        min_value = value
                        value_index = index
                        is_found = True
        if is_found:
            print(value_index)
        else:
            print("No matches")

    elif command[0] == "first":
        count = int(command[1])
        if command[2] == "even":
            if count > len(numbers):
                print("Invalid count")
            else:
                print(even_numbers[:count])
        elif command[2] == "odd":
            if count > len(numbers):
                print("Invalid count")
            else:
                print(odd_numbers[:count])

    elif command[0] == "last":
        count = int(command[1])
        if command[2] == "even":
            if count > len(numbers):
                print("Invalid count")
            else:
                print(even_numbers[-count:])
        elif command[2] == "odd":
            if count > len(numbers):
                print("Invalid count")
            else:
                print(odd_numbers[-count:])

    command = input().split()

print(numbers)
