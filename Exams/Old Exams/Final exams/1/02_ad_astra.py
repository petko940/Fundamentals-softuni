import re

pattern = re.compile(r"([\#|\|])([A-Za-z ]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1")

text = input()
total_calories = 0
# 2000kcal a day.
matches = pattern.findall(text)
output = []
for match in matches:
    total_calories += int(match[3])
    output.append(f"Item: {match[1]}, Best before: {match[2]}, Nutrition: {match[3]}")

days = total_calories // 2000
print(f"You have food to last you for: {days} days!")
[print(x) for x in output]


# import re
#
# text = input()
#
# pattern = re.compile(r"(?P<split>[/|#])(?P<item>[A-Za-z ]+)(?P=split)"
#                      r"(?P<date>\d{2}/\d{2}/\d{2})(?P=split)(?P<calories>\d{1,5})(?P=split)")
#
# matches = pattern.finditer(text)
# result = []
# average = 0
# for match in matches:
#     if 0 <= int(match['calories']) <= 10000:
#         result.append(f"Item: {match['item']}, Best before: {match['date']}, Nutrition: {match['calories']}")
#         average += int(match['calories'])
#
# days = average // 2000
# print(f"You have food to last you for: {days} days!")
# print("\n".join(result))
