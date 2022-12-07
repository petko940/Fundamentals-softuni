two_strings = input().split()
str1 = two_strings[0]
str2 = two_strings[1]
total_sum = 0

a = min(len(str1), len(str2))
for i in range(a):
    total_sum += ord(str1[i]) * ord(str2[i])

if len(str1) != len(str2):
    if len(str1) > len(str2):
        str1 = str1[a:]
        for i in range(len(str1)):
            total_sum += ord(str1[i])
    else:
        str2 = str2[a:]
        for i in range(len(str2)):
            total_sum += ord(str2[i])

print(total_sum)
