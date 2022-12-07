statistics = {
    "result": {},
    "submissions": {}
}

while True:
    command = input()
    if "exam finished" in command:
        break
    if "banned" in command:
        command = command.split("-")
        username = command[0]
        statistics["result"].pop(username)
    else:
        # username, language, points = [int(x) if x.isdigit() else x for x in command.split("-")]
        command = command.split("-")
        username = command[0]
        language = command[1]
        points = int(command[2])
        if username not in statistics["result"]:
            statistics["result"][username] = points
        else:
            if statistics["result"][username] < points:
                statistics["result"][username] = points
        if language not in statistics["submissions"]:
            statistics["submissions"][language] = 0
        statistics["submissions"][language] += 1

print("Results:")
for key in statistics["result"]:
    print(f"{key} | {statistics['result'][key]}")
print("Submissions:")
for key in statistics["submissions"]:
    print(f"{key} - {statistics['submissions'][key]}")
