def swap(index1, index2, list_):
    list_[index1], list_[index2] = list_[index2], list_[index1]
    return list_


def multiply(index1, index2, list_):
    list_[index1] *= list_[index2]
    return list(list_)


def decrease(list_):
    # list_ = [x - 1 for x in list_]
    list_ = list(map(lambda x: x - 1, list_))
    return list_


array = [int(x) for x in input().split()]

command = input()
while "end" not in command:
    command = command.split()
    if "swap" in command:
        index_one = int(command[1])
        index_two = int(command[2])
        swap(index_one, index_two, array)
    elif "multiply" in command:
        index_one = int(command[1])
        index_two = int(command[2])
        multiply(index_one, index_two, array)
    elif "decrease" in command:
        array = decrease(array)
    command = input()

print(*array, sep=", ")
