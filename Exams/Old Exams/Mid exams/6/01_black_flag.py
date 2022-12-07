days, plunder_for_a_day, expected_plunder = int(input()), int(input()), float(input())

total_plunder = 0
for current_day in range(1, days + 1):
    total_plunder += plunder_for_a_day
    if current_day % 3 == 0:
        total_plunder += plunder_for_a_day * 0.5

    if current_day % 5 == 0:
        total_plunder -= total_plunder * 0.3

percentage = (total_plunder / expected_plunder) * 100

if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {percentage:.2f}% of the plunder.")
