import re

text = input()
pattern = r"\ ([a-z0-9]+[a-z0-9\.\-\_]*@[a-z\-]+[a-z\.]*\.[a-z]+)"
match = re.findall(pattern, text)

for m in match:
    print(m)
