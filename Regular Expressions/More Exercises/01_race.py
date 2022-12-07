import re

pattern_name = re.compile(r"([A-Za-z])")
pattern_numbers = re.compile(r"(\d)")

racers = input().split(", ")
data_racers = {}
while True:
    participant = input()
    if "end of race" in participant:
        break
    name = pattern_name.findall(participant)
    name = "".join(name)
    if name in racers:
        numbers = pattern_numbers.findall(participant)
        numbers = sum([int(x) for x in numbers])
        data_racers[name] = data_racers.get(name, 0)
        data_racers[name] += numbers

output = []
for key, value in sorted(data_racers.items(), key=lambda item: -item[1]):
    output.append(key)

print(f"""1st place: {output[0]}
2nd place: {output[1]}
3rd place: {output[2]}
""")


# import re
#
# participants = input().split(", ")
#
# participants_stored = {}
# for participant in participants:
#     participants_stored[participant] = 0
#
# while True:
#     info = input()
#     lst = []
#     if info == "end of race":
#         break
#     for i in participants_stored.keys():
#         name_split = i
#         for x in name_split:
#             lst.append(x)
#             lst.append("?")
#
#         pattern = "".join(lst)
#         match_name = re.findall(pattern, info)
#         match_name = "".join(match_name)
#         points = 0
#         if i in match_name:
#             for point in info:
#                 if point.isdigit():
#                     points += int(point)
#             participants_stored[match_name] += points
#         lst.clear()
#
# output = []
# for key, value in sorted(participants_stored.items(), key=lambda x: -x[1]):
#     output.append(key)
#
# print(f"""1st place: {output[0]}
# 2nd place: {output[1]}
# 3rd place: {output[2]}""")
