import itertools

lst = [x for x in input().split(", ")]
count = itertools.count(0)
counter = 0

for i in lst:
    counter += 1
    if i == "wolf":
        (next(count))
        counter = 0

if lst[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {counter}! You are about to be eaten by a wolf!")

# a = [(next(count)) for x in lst if x == "sheep"]