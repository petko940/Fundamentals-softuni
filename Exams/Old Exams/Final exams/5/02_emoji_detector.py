import re

text = input()

pattern = re.compile(r"(?P<sep>::|\*\*)(?P<emoji>[A-Z][a-z]{2,})(?P=sep)")

numbers = [int(x) for x in text if x.isdigit()]
cool_threshold = 1
for x in numbers:
    cool_threshold *= x

matches = pattern.findall(text)

output = []
for match in matches:
    ascii_values = 0
    for char in match[1]:
        ascii_values += ord(char)
    if ascii_values > cool_threshold:
        output.append(f"{match[0]}{match[1]}{match[0]}")

print(f"""Cool threshold: {cool_threshold}
{len(matches)} emojis found in the text. The cool ones are:""")
[print(x) for x in output]


# import re
#
# strings = input()
#
# pattern_number = re.compile(r"\d")
# numbers = pattern_number.findall(strings)
# cool_threshold_sum = 1
# for n in numbers:
#     cool_threshold_sum *= int(n)
#
# pattern_emoji = re.compile(r"([:*]{2})(?P<emoji>[A-Z][a-z]{2,})(\1)")
# emojis = pattern_emoji.findall(strings)
# output = []
# for emoji in emojis:
#     output.append(f"{emoji[0]}{emoji[1]}{emoji[2]}")
#
# print(f"Cool threshold: {cool_threshold_sum}")
# print(f"{len(output)} emojis found in the text. The cool ones are:")
#
# for x in output:
#     y = x[2:-2]
#     count_ascii = 0
#     for char in y:
#         count_ascii += ord(char)
#     if count_ascii >= cool_threshold_sum:
#         print(x)
