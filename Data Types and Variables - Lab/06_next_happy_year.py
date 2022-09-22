year = input()
next_happy_year = False

while not next_happy_year:
    year = int(year) + 1
    year = str(year)
    happy_year = set()
    for i in range(len(year)):
        happy_year.add(year[i])
    if len(happy_year) == len(year):
        next_happy_year = True

print(year)
