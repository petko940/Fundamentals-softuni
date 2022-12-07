text = input()

encrypted_version = []
for char in text:
    new_char = ord(char) + 3
    encrypted_version.append(chr(new_char))

print("".join(encrypted_version))
