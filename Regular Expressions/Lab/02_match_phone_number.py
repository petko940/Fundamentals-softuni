import re

text= input()
pattern = re.compile(r"\+359([ |-])2\1\d{3}\1\d{4}\b")
# pattern = r"\+359(?P<sep> |-)2(?P=sep)\d{3}(?P=sep)\d{4}\b")

match = pattern.findall(text)
for m in match:
    pass