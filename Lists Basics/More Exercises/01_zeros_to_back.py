integers = [int(x) for x in input().split(", ")]
front = [x for x in integers if x > 0]
back = [x for x in integers if x == 0]

print(front + back)
