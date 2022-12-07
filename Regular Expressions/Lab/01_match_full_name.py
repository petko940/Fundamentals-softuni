import re

text = input()
pattern = re.compile(r"\b[A-Z][a-z]+\ [A-Z][a-z]+\b")

matches = pattern.findall(text)
print(" ".join(matches))
