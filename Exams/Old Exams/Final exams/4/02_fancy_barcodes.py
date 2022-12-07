import re

pattern = re.compile(r"@\#+([A-Z][A-Za-z0-9]{4,}[A-Z])@\#+")
pattern_numbers = re.compile(r"\d")

n = int(input())
for x in range(n):
    barcode = input()
    match = pattern.findall(barcode)
    match_numbers = pattern_numbers.findall(barcode)
    if match:
        if match_numbers:
            print(f"Product group: {''.join(match_numbers)}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")


# import re
#
# pattern = re.compile(r"@#+(?P<text>[A-Z][A-Za-z0-9]{4,}[A-Z])@#+")
# n = int(input())
# for _ in range(n):
#     barcode = input()
#     match = pattern.findall(barcode)
#     if match:
#         digits = ""
#         for m in match[0]:
#             if m.isdigit():
#                 digits += m
#         if digits:
#             print(f"Product group: {digits}")
#         else:
#             print("Product group: 00")
#     else:
#         print("Invalid barcode")