number_of_snowballs = int(input())

max_value = 0
weight = 0
time_needed = 0
quality = 0
for _ in range(number_of_snowballs):
    current_weight = int(input())
    current_time_needed = int(input())
    current_quality = int(input())
    current_value = (current_weight / current_time_needed) ** current_quality
    if current_value >= max_value:
        max_value = current_value
        weight = current_weight
        time_needed = current_time_needed
        quality = current_quality

print(f"{weight} : {time_needed} = {round(max_value)} ({quality})")
