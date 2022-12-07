text = input()
strength = 0
new_text = []

for n in range(len(text)):
    if strength > 0 and text[n] != ">":
        strength -= 1
    elif text[n] == ">":
        new_text.append(text[n])
        strength += int(text[n + 1])
    elif text[n] != ">":
        new_text.append(text[n])

print("".join(new_text))
