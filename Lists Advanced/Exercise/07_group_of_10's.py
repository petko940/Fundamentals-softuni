numbers = [int(x) for x in input().split(", ")]

new_list = []
group = 10

while len(numbers) > 0:
    filtered_list = filter(lambda x: x <= group, numbers)
    print(f"Group of {group}'s: {list(filtered_list)}")
    numbers = [x for x in numbers if x > group]
    new_list.clear()
    group += 10
