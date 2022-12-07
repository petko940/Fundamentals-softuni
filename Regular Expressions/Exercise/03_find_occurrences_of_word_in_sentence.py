import re

string = input().lower()
checked_word = input().lower()

patterns = re.compile(r"\b" + checked_word + r"\b")
matches = patterns.finditer(string)

result = 0
for word in matches:
    result += 1
print(result)

