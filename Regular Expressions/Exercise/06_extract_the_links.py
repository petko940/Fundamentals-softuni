import re

pattern = r"(www\.[a-zA-Z0-9\-]+[\.a-z]*\.[a-z]+)"
text = input()
while text:
    match = re.findall(pattern, text)
    [print(x) for x in match]
    text = input()
