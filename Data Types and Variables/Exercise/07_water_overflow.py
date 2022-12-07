n = int(input())

water_tank = 0
for _ in range(n):
    liters_of_water = int(input())
    water_tank += liters_of_water
    if water_tank > 255:
        print("Insufficient capacity!")
        water_tank -= liters_of_water

print(water_tank)
