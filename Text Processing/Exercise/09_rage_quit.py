text = input()
new_text = ""
temp_text = ""
temp_number = ""
for n in range(len(text)):
    if not text[n].isdigit():
        temp_text += text[n]
    else:
        temp_number += text[n]
        if n + 1 < len(text):
            if text[n + 1].isdigit():
                continue
        number = int(temp_number)
        temp_text = number * temp_text
        new_text += temp_text
        temp_text, temp_number = "", ""

new_text = new_text.upper()
print(f"Unique symbols used: {len(set(new_text))}")
print(new_text)

