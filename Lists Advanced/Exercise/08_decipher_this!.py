secret_message = input().split()

output = []
for current_message in secret_message:
    digits = []
    count = 0
    split_message = [x for x in current_message]
    for i in split_message:
        if i.isdigit():
            digits.append(i)
            count += 1
    ascii_char = int("".join(digits))
    char = chr(ascii_char)
    split_message = split_message[count:]
    split_message.insert(0, char)
    split_message[1], split_message[-1] = split_message[-1], split_message[1]
    output.append(split_message)

for current_word in output:
    print("".join(current_word), end=" ")
