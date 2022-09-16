divisor, boundary = int(input()), int(input())

for i in range(boundary, 0, -1):
    if i % divisor == 0 and boundary >= i > 0:
        print(i)
        break
