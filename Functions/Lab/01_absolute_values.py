def absolute_value():
    numbers = [float(x) for x in input().split()]
    result = list(map(abs, numbers))
    return result


print(absolute_value())

