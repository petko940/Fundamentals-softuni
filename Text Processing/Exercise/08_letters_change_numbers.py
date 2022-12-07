from string import ascii_uppercase, ascii_lowercase

string = input().split()
letter = []
numbers = []
total_sum = 0

for n in string:
    first_letter,last_letter = n[0],n[-1]
    current_number = int(n[1:-1])
    current_sum= 0
    if first_letter.isupper():
        current_sum = current_number / (ascii_uppercase.index(first_letter) + 1)
    elif first_letter[0].islower():
        current_sum = current_number * (ascii_lowercase.index(first_letter) + 1)

    if last_letter.isupper():
        current_sum = current_sum - (ascii_uppercase.index(last_letter) + 1)
    elif last_letter.islower():
        current_sum = current_sum + (ascii_lowercase.index(last_letter) + 1)

    total_sum += current_sum

print(f"{total_sum:.2f}")
