dictionary = {}
text = input().split()
text = "".join(text)

for char in text:
    if char not in dictionary:
        dictionary[char] = 0
    dictionary[char] += 1

[print(f"{char} -> {occurrences}") for char, occurrences in dictionary.items()]


# string = input().split()
# dictionary = {}
#
# for char in string:
#     split = [x for x in char]
#     for x in split:
#         if x not in dictionary:
#             dictionary[x] = 0
#         dictionary[x] += 1
#
# for k, v in dictionary.items():
#     print(f"{k} -> {v}")
