import re

text = input()

pattern = re.compile(r"(?P<a>[=|\/])(?P<city>[A-Z][A-Za-z]{2,})(?P=a)")
matches = pattern.finditer(text)

destinations = []
total_points = 0
for match in matches:
    destinations.append(f"{match['city']}")
    total_points += len(match['city'])

print("Destinations: ", end="")
print(", ".join(destinations))
print(f"Travel Points: {total_points}")
