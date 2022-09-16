n = int(input())

opening_count = 0
closing_count = 0
for i in range(n):
    command = input()
    if command == "(":
        opening_count += 1
    elif command == ")":
        closing_count += 1
    if opening_count > closing_count + 1 or opening_count < closing_count:
        print("UNBALANCED")
        break
else:
    print("BALANCED")

