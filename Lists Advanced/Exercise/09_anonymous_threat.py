def merge(start_index, end_index, array):
    if start_index < 0:
        start_index = 0
    if end_index >= len(array):
        end_index = len(array) - 1
    if 0 <= start_index < len(array) and 0 <= end_index < len(array):
        taken_array = "".join(array_of_data[start_index:end_index + 1])
        del array_of_data[start_index:end_index + 1]
        array.insert(start_index, taken_array)
        return array


def divide(index, substrings, array):
    if substrings >= len(array[index]):
        step = 1
    else:
        step = len(array[index]) // substrings
    taken_array = array.pop(index)
    start_part = 0
    for i in range(substrings):
        if i == substrings - 1:
            array.insert(index, taken_array[start_part::])
            break
        else:
            array.insert(index, taken_array[start_part:start_part + step])
        start_part += step
        index += 1


array_of_data = input().split()

commands = input()
while "3:1" not in commands:
    commands = commands.split()
    if "merge" in commands:
        position = int(commands[1])
        end = int(commands[2])
        merge(position, end, array_of_data)
    elif "divide" in commands:
        position = int(commands[1])
        end = int(commands[2])
        divide(position, end, array_of_data)
    commands = input()

print(" ".join(array_of_data))
