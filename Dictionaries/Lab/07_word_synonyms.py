n = int(input())
synonyms = {}

for _ in range(n):
    word, synonym = input(), input()
    if word in synonyms.keys():
        synonyms[word] += ", " + synonym
        continue
    synonyms[word] = synonym

for key, value in synonyms.items():
    print(f"{key} - {value}")
