number_students = int(input())
number_lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
biggest = 0
for i in range(number_students):
    count_of_attendances = int(input())
    if count_of_attendances > biggest:
        biggest = count_of_attendances
    total_bonus = count_of_attendances / number_lectures *(5 + additional_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus

print(f"""Max Bonus: {round(max_bonus)}.
The student has attended {biggest} lectures.""")
