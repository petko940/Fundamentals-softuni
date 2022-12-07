employees = [int(x) for x in input().split()]
factor = int(input())

employees_happiness = list(map(lambda x: x * factor, employees))
average_happiness = sum(employees_happiness) / len(employees)

filter = [x for x in employees_happiness if x > average_happiness]

print(f"Score: {len(filter)}/{len(employees)}.", end=" ")

if len(filter) < average_happiness:
    print("Employees are not happy!")
else:
    print("Employees are happy!")
