def data_types(type: str, number):
    if type == "int":
        number = int(number) * 2
    elif type == "real":
        number = float(number) * 1.5
        number = str(f"{number:.2f}")
    elif type == "string":
        number = "$" + number + "$"
    return number


strings_one = input()
strings_two = input()
print(data_types(strings_one, strings_two))
