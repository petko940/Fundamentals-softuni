start, end = ord(input()), ord(input())

text = input()
total_sum = []
for char in text:
    if start < ord(char) < end:
        total_sum.append(ord(char))

print(sum(total_sum))
