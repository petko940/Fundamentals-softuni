students = input()
data = {}

while ":" in students:
    students = students.split(":")
    data[int(students[1])] = students[0], students[2]
    students = input()

students = students.replace("_", " ")

for key, value in data.items():
    if students in value:
        print(f"{value[0]} - {key}")
