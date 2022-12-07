n = int(input())
word = input()

lst = list()
filtered = list()

for i in range(n):
    lst.append(input())
    if word in lst[i]:
        filtered.append(lst[i])

print(lst)
print(filtered)
