factor = int(int(input()))
count = int(int(input()))

lst = [x for x in range(factor, factor * count + 1, factor)]
print(lst)
