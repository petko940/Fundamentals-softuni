def tribonacci(number: int):
    lst = [1, 1, 2]
    if number == 1:
        return [1]
    elif number == 2:
        return [1, 1]
    for i in range(3, number):
        # lst.append(lst[-1] + lst[-2] + lst[-3])
        lst.append(sum(lst[-1:-4:-1]))
    return lst


num = int(input())
print(*tribonacci(num))
