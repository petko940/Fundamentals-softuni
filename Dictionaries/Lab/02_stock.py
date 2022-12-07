data = input().split()
search = input().split()

stock = {}
for i in range(0, len(data), 2):
    key = data[i]
    value = data[i + 1]
    stock[key] = value

output = []
for x in search:
    if x in stock:
        output.append(f"We have {stock[x]} of {x} left")
    else:
        output.append(f"Sorry, we don't have {x}")

print("\n".join(output))
