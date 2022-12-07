def function():
    global amount_of_water, effort, total_fire
    amount_of_water -= value_of_cells
    effort += value_of_cells * 0.25
    total_fire += value_of_cells
    print(f" - {value_of_cells}")


fire_and_cells = input().split("#")
amount_of_water = int(input())

effort = 0
total_fire = 0
print("Cells:")
for current_cell in fire_and_cells:
    current_cell = current_cell.split(" = ")
    type_fire = current_cell[0]
    value_of_cells = int(current_cell[1])
    if amount_of_water < value_of_cells:
        continue
    if "High" in type_fire and 81 <= value_of_cells <= 125 \
            or "Medium" in type_fire and 51 <= value_of_cells <= 80 \
            or "Low" in type_fire and 1 <= value_of_cells <= 50:
        function()

print(f"""Effort: {effort:.2f}
Total Fire: {total_fire}
""")
