number = int(input())

for i in range(number):
    string = input()
    if "." in string or "," in string or "_" in string:
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")
