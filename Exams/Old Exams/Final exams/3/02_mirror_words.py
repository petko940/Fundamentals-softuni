import re

text = input()

# pattern = re.compile(r"(?P<sep>@|#)(?P<word1>[A-Za-z]{3,})(?P=sep){2}(?P<word2>[A-Za-z]{3,})")
pattern = re.compile(r"(\@|\#)([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1")
matches = pattern.finditer(text)
count = 0
pairs = []
for match in matches:
    count += 1
    if match[2] == match[3][::-1]:
        pairs.append(f"{match[2]} <=> {match[3]:}")


if count:
    print(f"{count} word pairs found!")
else:
    print("No word pairs found!")

if pairs:
    print("The mirror words are:")
    print(", ".join(pairs))
else:
    print("No mirror words!")