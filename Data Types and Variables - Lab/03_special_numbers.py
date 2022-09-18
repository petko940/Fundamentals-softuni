n = int(input())
sum_digits = 0
for i in range(1,n+1):
    while i > 0:
        sum_digits += i % 10
        i /= 10

    if sum_digits == 5 or sum_digits == 7 or sum_digits == 1:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")
