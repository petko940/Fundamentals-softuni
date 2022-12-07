n = int(input())

positives = list()
negatives = list()

for _ in range(n):
    new_element = int(input())
    if new_element >= 0:
        positives.append(new_element)
    else:
        negatives.append(new_element)

print(positives)
print(negatives)
print(f"""Count of positives: {len(positives)}
Sum of negatives: {sum(negatives)}""")
