import re

pattern = re.compile(r"[starSTAR]")

n = int(input())
attacked_planet = []
destroyed_planets = []

for _ in range(n):
    text = input()
    matches = pattern.findall(text)
    new_text = ""
    for x in text:
        a = chr(ord(x) - len(matches))
        new_text += a

    info_pattern = r"@([A-Za-z]+)[^\@\-\!\:]*:(\d+)[^\@\-\!\:]*!(A|D)![^\@\-\!\:]*->(\d+)"
    info_matches = re.search(info_pattern, new_text)
    if info_matches:
        if info_matches.group(3) == "A":
            attacked_planet.append(info_matches.group(1))
        elif info_matches.group(3) == "D":
            destroyed_planets.append(info_matches.group(1))

attacked_planet = sorted(attacked_planet)
destroyed_planets = sorted(destroyed_planets)
print(f"Attacked planets: {len(attacked_planet)}")
[print(f"-> {x}") for x in attacked_planet]
print(f"Destroyed planets: {len(destroyed_planets)}")
[print(f"-> {x}") for x in destroyed_planets]
