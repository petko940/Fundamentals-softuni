import re

places = input()

pattern = r"([=\/])([A-Z][A-Za-z]{2,})\1"

matches = re.finditer(pattern, places)

destinations = {}
for match in matches:
    destinations[match.group(2)] = len(match.group(2))

print(f"Destinations: {', '.join(destinations.keys())}")
print(f"Travel Points: {sum(destinations.values())}")