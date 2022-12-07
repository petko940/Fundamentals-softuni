import re

pattern = re.compile(r"%(?P<name>[A-Z][a-z]+)%([^\|\$\%\.]*)"
                     r"<(?P<product>\w+)>([^\|\$\%\.]*)\|"
                     r"(?P<count>[0-9]+)\|([^\|\$\%\.]*)"
                     r"(?P<real>[1-9]+[.0-9]*)\$")
total_sum = 0
result = []
while True:
    lines = input()
    if lines == "end of shift":
        break

    matches = pattern.finditer(lines)
    for match in matches:
        total_price = int(match['count']) * float(match['real'])
        result.append(f"{match['name']}: {match['product']} - {total_price:.2f}")
        total_sum += total_price

print("\n".join(result))
print(f"Total income: {total_sum:.2f}")
