import re

text = input()

pattern = re.compile(r"\b_(?P<word>[A-Za-z0-9]+\b)")
match = re.findall(pattern, text)

print(",".join(match))


# import re
#
# text = input()
#
# pattern = r"\b_(?P<word>[a-zA-z0-9]+\b)"
# match = re.findall(pattern, text)
# lst = []
# for x in match:
#     lst.append(x)
#
# print(",".join(lst))
