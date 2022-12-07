array = [int(x) for x in input().split()]

average = 0
for i in array:
    average += i
average /= len(array)
array.sort(reverse=True)

array = [x for x in array if x > average]
if len(array) > 5:
    [print(array[x], end=" ") for x in range(5)]
elif len(array) == 0:
    print("No")
else:
    print(*array)
