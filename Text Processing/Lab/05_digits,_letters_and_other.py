filtered = {
    "digits": [],
    "letters": [],
    "other": []
}

text = input()
for char in text:
    if char.isdigit():
        filtered["digits"].append(char)
    elif char.isalpha():
        filtered["letters"].append(char)
    else:
        filtered["other"].append(char)

for value in filtered.values():
    print("".join(value))
