from string import ascii_letters,digits
username = input().split(", ")

output = []
for x in username:
    flag = True
    split_word = [split for split in x]
    for i in split_word:
        if i not in "-_" + ascii_letters + digits:
            flag = False
    if 3 <= len(x) <= 16 \
        and flag:
        output.append(x)

print("\n".join(output))
