import re

pattern = re.compile(">>(\w+)<<(\d+[\.\d]*)!(\d+)")
data = []
while True:
    information = input()
    if information == "Purchase":
        break
    match = pattern.findall(information)
    data.append(match)

total_money = 0
print("Bought furniture:")

for x in data:
    if x:
        print(x[0][0])
        total_money += float(x[0][1]) * int(x[0][2])

print(f"Total money spend: {total_money:.2f}")
