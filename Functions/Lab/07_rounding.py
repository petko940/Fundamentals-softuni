# result = list(map(lambda x: round(float(x)), input().split()))
result = [round(float(x)) for x in input().split()]
print(result)