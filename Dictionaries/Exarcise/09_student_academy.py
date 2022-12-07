data = {}

n = int(input())
for current in range(n):
    student_name, grade = input(), float(input())
    if student_name not in data:
        data[student_name] = []
    data[student_name].append(grade)

for key, value in data.items():
    average = sum(value) / len(value)
    if average >= 4.50:
        print(f"{key} -> {average:.2f}")
