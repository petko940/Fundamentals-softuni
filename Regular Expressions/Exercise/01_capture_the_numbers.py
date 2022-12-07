import re

pattern = r"\d+"
while True:
    line = input()
    if line:
        match = re.findall(pattern, line)
        for x in match:
            print(x, end=" ")
    else:
        break
