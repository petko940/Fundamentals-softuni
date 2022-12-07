key = [int(x) for x in input().split()]

while True:
    text = input()
    if text == "find":
        break

    txt = ""
    index = 0
    for char in text:
        txt += chr(ord(char) - key[index])
        index += 1
        if index >= len(key):
            index = 0

    indexes_type_treasure = [i for i, v in enumerate(txt) if v == "&"]
    start_index_type, end_index_type = indexes_type_treasure[0], indexes_type_treasure[1]
    start_coordinate, end_coordinate = 0, 0
    for i, v in enumerate(txt):
        if v == "<":
            start_coordinate = i
        if v == ">":
            end_coordinate = i

    print(f"Found {txt[start_index_type + 1:end_index_type]} at {txt[start_coordinate + 1:end_coordinate]}")
