money = [int(x) for x in input().split(", ")]
beggars = int(input())
new_list = list()
index = 0
for i in range(beggars):
    sum_money = 0
    for beg in range(index, len(money), beggars):
        sum_money += money[beg]
    new_list.append(sum_money)
    index += 1

print(new_list)

# numbers = [int(x) for x in input().split(", ")]
# beggars = int(input())
# count = 0
# new_numbers = [0] * beggars
#
# for i in numbers:
#     new_numbers[count] += i
#     count += 1
#     if count >= beggars:
#         count = 0
#
# print(new_numbers)
