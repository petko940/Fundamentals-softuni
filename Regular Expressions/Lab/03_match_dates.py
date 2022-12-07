import re

dates = input()
pattern = re.compile(r"\b(\d{2})(/|-|.)([A-Z][a-z]{2})\2(\d{4})\b")

matches = pattern.finditer(dates)
for match in matches:
    print(f"Day: {match.group(1)}, Month: {match.group(3)}, Year: {match.group(4)}")
# import re
#
# date = input()
# regex = re.compile(r"(?P<date>\d{2})(?P<sep>[.|/|-])(?P<month>[A-Z][a-z]{2})(?P=sep)(?P<year>\d{4})")
# match = re.finditer(regex, date)
#
# for x in match:
#     print(f"Day: {x['date']}, Month: {x['month']}, Year: {x['year']}")
