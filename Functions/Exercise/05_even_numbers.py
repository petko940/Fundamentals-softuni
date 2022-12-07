# def even_numbers(number):
#     if number % 2 == 0:
#         return True
#
#
# numbers = list(map(int, input().split()))
# even_number = filter(even_numbers, numbers)
# print(list(even_number))


numbers = [int(i) for i in input().split()]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))
