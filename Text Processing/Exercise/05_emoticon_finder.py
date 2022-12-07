text = input()

for index in range(len(text)):
    if text[index] == ':':
        print(text[index] + text[index + 1])


# text = input()
#
# for index, value in enumerate(text):
#     if value == ":":
#         print(value + text[index+1])
