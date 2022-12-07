def drive(car, distance, fuel, car_info):
    if car_info["car"][car]["fuel"] < fuel:
        print("Not enough fuel to make that ride")
    else:
        car_info["car"][car]["mileage"] += distance
        car_info["car"][car]["fuel"] -= fuel
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if car_info["car"][car]["mileage"] >= 100000:
            del car_info["car"][car]
            print(f"Time to sell the {car}!")


def refuel(car, fuel, car_info):
    current_fuel = car_info["car"][car]["fuel"]
    temp = current_fuel
    current_fuel += fuel
    if current_fuel > 75:
        current_fuel = 75
        fuel = abs(temp - current_fuel)
    print(f"{car} refueled with {fuel} liters")
    car_info["car"][car]["fuel"] = current_fuel


def revert(car, kilometers, car_info):
    car_info["car"][car]["mileage"] -= kilometers
    if car_info["car"][car]["mileage"] < 10000:
        car_info["car"][car]["mileage"] = 10000
    else:
        print(f"{car} mileage decreased by {kilometers} kilometers")


def main():
    car_info = {"car": {}}
    number_of_cars = int(input())
    for _ in range(number_of_cars):
        car, mileage, fuel = [int(x) if x.isdigit() else x for x in input().split("|")]
        car_info["car"][car] = {"mileage": mileage, "fuel": fuel}
    while True:
        command = input()
        if "Stop" in command:
            break
        event, car, *data = [int(x) if x.isdigit() else x for x in command.split(" : ")]
        if event == "Drive":
            drive(car, *data, car_info)
        elif event == "Refuel":
            refuel(car, *data, car_info)
        elif event == "Revert":
            revert(car, *data, car_info)

    for key, value in car_info['car'].items():
        print(f"{key} -> Mileage: {value['mileage']} kms, Fuel in the tank: {value['fuel']} lt.")


main()
