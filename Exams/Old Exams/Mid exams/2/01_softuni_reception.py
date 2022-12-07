first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
student_count = int(input())

time_count = 0

while student_count > 0:
    time_count += 1
    if time_count % 4 == 0:
        time_count += 1
    student_count -= first_employee_efficiency + second_employee_efficiency + third_employee_efficiency

print(f"Time needed: {time_count}h.")
