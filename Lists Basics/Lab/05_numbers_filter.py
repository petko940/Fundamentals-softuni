n = int(input())
numbers = list()

for _ in range(n):
    numbers.append(int(input()))

command = input()

output = list()
if command == "even":
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            output.append(numbers[i])
elif command == "odd":
    for i in range(len(numbers)):
        if numbers[i] % 2 != 0:
            output.append(numbers[i])
elif command == "negative":
    for i in range(len(numbers)):
        if numbers[i] < 0:
            output.append(numbers[i])
elif command == "positive":
    for i in range(len(numbers)):
        if numbers[i] >= 0:
            output.append(numbers[i])

print(output)


# number_of_lines = int(input())
#
# # constant values
# COMMAND_EVEN = 'even'
# COMMAND_ODD = 'odd'
# COMMAND_POSITIVE = 'positive'
# COMMAND_NEGATIVE = 'negative'
#
# # accepting numbers from user input
# numbers = []
#
# for _ in range(number_of_lines):
#     current_number = int(input())
#     numbers.append(current_number)
#
# command = input()
#
# filtered_numbers = []
#
# # number_filtering
# for number in numbers:
#     filtered_passes = (
#             (command == COMMAND_EVEN and number % 2 == 0) or
#             (command == COMMAND_ODD and number % 2 != 0) or
#             (command == COMMAND_NEGATIVE and number < 0) or
#             (command == COMMAND_POSITIVE and number >= 0)
#     )
#     if filtered_passes:
#         filtered_numbers.append(number)
#
# print(filtered_numbers)
