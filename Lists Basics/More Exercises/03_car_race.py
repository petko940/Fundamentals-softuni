numbers = [int(x) for x in input().split()]

finish = len(numbers) // 2
left = list(numbers[:finish])
left_sum = 0
for left_current_time in range(len(left)):
    if left[left_current_time] == 0:
        left_sum *= 0.8
    left_sum += left[left_current_time]

right = list(numbers[finish + 1:])
right_sum = 0
for right_current_time in range(finish - 1, -1, -1):
    if right[right_current_time] == 0:
        right_sum *= 0.8
    right_sum += right[right_current_time]

if left_sum > right_sum:
    print(f"The winner is right with total time: {right_sum:.1f}")
else:
    print(f"The winner is left with total time: {left_sum:.1f}")