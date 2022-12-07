numbers = [int(x) for x in input().split()]

output_sum = 0
while len(numbers):
    index = int(input())
    if 0 <= index < len(numbers):
        removed_element = numbers.pop(index)
    elif index < 0:
        removed_element = numbers.pop(0)
        numbers.insert(0, numbers[-1])
    elif index >= len(numbers):
        removed_element = numbers.pop(-1)
        numbers.append(numbers[0])

    output_sum += removed_element
    # for num in range(len(numbers)):
    #     if numbers[num] > removed_element:
    #         numbers[num] -= removed_element
    #     else:
    #         numbers[num] += removed_element
    numbers = [numbers[x] - removed_element if numbers[x] > removed_element
               else numbers[x] + removed_element for x in range(len(numbers))]

print(output_sum)
