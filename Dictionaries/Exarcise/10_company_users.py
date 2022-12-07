data = {}

information = input()
while "End" not in information:
    company_names, employees_id = information.split(" -> ")
    if company_names not in data:
        data[company_names] = []
    if employees_id not in data[company_names]:
        data[company_names].append(employees_id)
    information = input()

for key, value in data.items():
    print(key)
    for current_value in value:
        print(f"-- {current_value}")
