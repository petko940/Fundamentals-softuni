numbers = [int(x) for x in input().split(", ")]
positives = [str(positive) for positive in numbers if positive >= 0]
negatives = [str(negative) for negative in numbers if negative < 0]
evens = [str(even) for even in numbers if even % 2 == 0]
odds = [str(odd) for odd in numbers if odd % 2 != 0]

print(f"""Positive: {", ".join(positives)}
Negative: {", ".join(negatives)}
Even: {", ".join(evens)}
Odd: {", ".join(odds)}
""")
