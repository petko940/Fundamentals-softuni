to_do = input().split("-")
tasks = []

while not to_do[0] in "End":
    priority = int(to_do[0])
    current_task = to_do[1]
    tasks.append((priority,current_task))
    to_do = input().split("-")

sorted_tasks = []
for task_data in sorted(tasks):
    sorted_tasks.append(task_data[1])

print(sorted_tasks)
