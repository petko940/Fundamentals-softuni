number_of_cities = int(input())

total_profit = 0

for current in range(1, number_of_cities + 1):
    name_city = input()
    money_earned = float(input())  # приход
    expenses = float(input())  # разход

    special_event = 0
    if current % 3 == 0:
        special_event += 0.50 * expenses
    if current % 5 == 0:
        special_event = 0
        money_earned -= 0.10 * money_earned

    current_profit = money_earned - expenses - special_event
    total_profit += current_profit

    print(f"In {name_city} Burger Bus earned {current_profit:.2f} leva.")

print(f"Burger Bus total profit: {total_profit:.2f} leva.")
