# data = {
#     "contest": {},
#     "individual_statistics": {}
# }
#
# command = input()
# while "no more time" not in command:
#     username, contest, points = [int(x) if x.isdigit() else x for x in command.split(" -> ")]
#     if contest not in data["contest"]:
#         data["contest"][contest] = {}
#
#     if username not in data["contest"][contest]:
#         data["contest"][contest][username] = points
#
#     if username not in data["individual_statistics"]:
#         data["individual_statistics"][username] = 0
#
#     if username in data["individual_statistics"] and data["contest"][contest][username] == points:
#         data["individual_statistics"][username] += points
#
#     if data["contest"][contest][username] < points:
#         data["individual_statistics"][username] += points - data["contest"][contest][username]
#
#     if data["contest"][contest][username] < points:
#         data["contest"][contest][username] = points
#
#     command = input()
#
# for key, value in data["contest"].items():
#     print(f"{key}: {len(value)} participants")
#     number = 1
#     for user in sorted(value.items(), key=lambda item: (-item[1], item[0])):
#         print(f"{number}. {user[0]} <::> {user[1]}")
#         number += 1
#
# print("Individual standings:")
# number = 1
# for value in sorted(data["individual_statistics"].items(), key=lambda item: (-item[1], item[0])):
#     print(f"{number}. {value[0]} -> {value[1]}")
#     number += 1


data = {
    'contests': {},
    'individual_statistics': {}
}

while True:
    command = input()
    if command == "no more time":
        break

    username, contest, points = [int(x) if x.isdigit() else x for x in command.split(' -> ')]
    if contest not in data['contests']:
        data["contests"][contest] = {}

    if username not in data['contests'][contest]:
        data['contests'][contest][username] = 0

    if data["contests"][contest][username] < points:
        data["contests"][contest][username] = points

    if username not in data["individual_statistics"]:
        data["individual_statistics"][username] = 0

for key, value in data['contests'].items():
    print(f"{key}: {len(value)} participants")
    n = 1
    for k, v in sorted(value.items(), key=lambda x: (-x[1], x[0])):
        print(f"{n}. {k} <::> {v}")
        n += 1


for key, value in data['contests'].items():
    for name, point in data['individual_statistics'].items():
        if name in value.keys():
            for k, v in value.items():
                if k == name:
                    data['individual_statistics'][name] += v
                    break

print(f"Individual standings:")
n = 1
for key, value in sorted(data['individual_statistics'].items(), key=lambda x: (-x[1], x[0])):
    print(f"{n}. {key} -> {value}")
    n += 1
