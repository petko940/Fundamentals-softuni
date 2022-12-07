def chars_between(char_start, char_end):
    # loop = []
    # for i in range(ord(char_start) + 1,ord(char_end)):
    #     loop.append(chr(i))
    loop = [chr(i) for i in range(ord(char_start) + 1, ord(char_end))]
    return " ".join(loop)


print(chars_between(input(), input()))
