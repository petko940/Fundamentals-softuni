string = input().lower()

check_words = ["sand", "water", "fish", "sun"]
count = 0
for i in range(4):
    count += string.count(check_words[i])
print(count)
