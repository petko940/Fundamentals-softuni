number_people = int(input())
capacity = int(input())

courses = number_people // capacity
number_people -= courses * capacity
if number_people:
    courses += 1

print(courses)


# from math import ceil
#
# number_of_people = int(input())
# elevator_capacity = int(input())
# number_of_courses = ceil(number_of_people / elevator_capacity)
# print(number_of_courses)