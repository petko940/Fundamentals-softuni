key = int(input())
n = int(input())

new_letter = list()
for i in range(n):
    letter = input()
    new_letter.append(chr(ord(letter) + key))

print("".join(new_letter))
