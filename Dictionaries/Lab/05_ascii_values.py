characters = input().split(", ")
dictionary = {}

for char in characters:
    dictionary[char] = ord(char)

print(dictionary)
