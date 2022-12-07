numbers = [int(x) for x in input().split()]

kill = int(input())
new_list = list()
index = 0
count = 0
num = len(numbers)
while len(new_list) < num:
    count += 1

    if count % kill == 0:
        new_list.append(numbers[index])
        numbers.pop(index)
    else:
        index += 1
    if index >= len(numbers):
        index = 0

print(str(new_list).replace(' ', ''))
