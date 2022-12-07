sequences_one = input().split(", ")
sequences_two = input().split(", ")

output = []

for seq1 in sequences_one:
    for seq2 in sequences_two:
        if seq1 in seq2:
            output.append(seq1)
            break

print(output)
