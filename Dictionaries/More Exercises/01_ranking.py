data = {
    "contest_data": {},
    "contest_points": {"name": {}}
}

while True:
    contest_password = input()
    if "end of contests" in contest_password:
        break
    contest, password_for_contest = contest_password.split(":")
    if contest not in data["contest_data"]:
        data["contest_data"][contest] = None
    data["contest_data"][contest] = password_for_contest

while True:
    usernames_password = input()
    if "end of submissions" in usernames_password:
        break
    contest, password, username, points = usernames_password.split("=>")
    points = int(points)
    if contest in data["contest_data"] and password in data["contest_data"][contest]:
        if username not in data["contest_points"]["name"]:
            data["contest_points"]["name"][username] = {}
            data["contest_points"]["name"][username][contest] = points
        elif username in data["contest_points"]["name"]:
            if contest in data["contest_points"]["name"][username]:
                if data["contest_points"]["name"][username][contest] < points:
                    data["contest_points"]["name"][username][contest] = points
            else:
                data["contest_points"]["name"][username][contest] = points

best_user = ""
most_points = 0
for name in data["contest_points"]["name"]:
    current_points = sum(data["contest_points"]["name"][name].values())
    if most_points < current_points:
        most_points = current_points
        best_user = name

print(f"Best candidate is {best_user} with total {most_points} points.\nRanking:")

for key in sorted(data["contest_points"]["name"]):
    print(key)
    for k, v in sorted(data["contest_points"]["name"][key].items(), key=lambda item: -item[1]):
        print(f"#  {k} -> {v}")
