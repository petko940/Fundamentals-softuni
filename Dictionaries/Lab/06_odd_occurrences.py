words = input().split()
dictionary = dict()

for word in words:
    lower = word.lower()
    if lower not in dictionary:
        dictionary[lower] = 0
    dictionary[lower] += 1

output = []
for key, value in dictionary.items():
    if value % 2 != 0:
        output.append(key)
print(*output)

