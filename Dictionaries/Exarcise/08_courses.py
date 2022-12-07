courses_data = {}

command = input()
while "end" not in command:
    course, student = command.split(" : ")
    if course not in courses_data:
        courses_data[course] = []
    courses_data[course].append(student)
    command = input()

for key, value in courses_data.items():
    print(f"{key}: {len(value)}")
    for data in value:
        print(f"-- {data}")

