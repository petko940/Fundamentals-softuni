def check_rooms(number_rooms):
    total_free_chairs = 0
    total_needed_chairs = 0
    for current_room in range(1, number_of_rooms + 1):
        free_chairs_number, people = input().split()
        free_chairs_number = len(free_chairs_number)
        people = int(people)
        if free_chairs_number >= people:
            total_free_chairs += free_chairs_number - people
        else:
            total_needed_chairs += people - free_chairs_number
            difference = people - free_chairs_number
            print(f"{difference} more chairs needed in room {current_room}")
    return total_free_chairs, total_needed_chairs


number_of_rooms = int(input())
total_free_chairs, total_needed_chairs = check_rooms(number_of_rooms)
if total_free_chairs >= total_needed_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")

# number_of_rooms = int(input())
#
# free_chairs = 0
# have_free_chairs = True
# chairs_need = []
# for current_room in range(1, number_of_rooms + 1):
#     room = input().split()
#     chairs = len(room[0])
#     if chairs >= int(room[1]):
#         free_chairs += chairs - int(room[1])
#     else:
#         needed_chairs_in_room = int(room[1]) - chairs
#         chairs_need.append(f"{needed_chairs_in_room} more chairs needed in room {current_room}")
#         have_free_chairs = False
#
# if have_free_chairs:
#     print(f"Game On, {free_chairs} free chairs left")
# else:
#     print(*chairs_need, sep="\n")
