numbers = [int(x) for x in input().split()]
n = int(input())

sorted_numbers = sorted(numbers)
for x in range(n):
    numbers.remove(sorted_numbers[x])

print(*numbers, sep=", ")
