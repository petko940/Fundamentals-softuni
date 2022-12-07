people_waiting = int(input())
state_of_the_lift = [int(x) for x in input().split()]

for current_wagon in range(len(state_of_the_lift)):
    if people_waiting == 0:
        break
    for x in range(4):
        if state_of_the_lift[current_wagon] < 4:
            people_waiting -= 1
            state_of_the_lift[current_wagon] += 1
        if state_of_the_lift[current_wagon] == 4 or people_waiting == 0:
            break

if people_waiting == 0 and any(x != 4 for x in state_of_the_lift):
    print(f"The lift has empty spots!")
elif people_waiting > 0:
    print(f"There isn't enough space! {people_waiting} people in a queue!")

print(*state_of_the_lift)


# people_waiting = int(input())
# lift_state = [int(i) for i in input().split()]
#
# for i in range(len(lift_state)):
#     if lift_state[i] < 4:
#         if people_waiting >= 4 - lift_state[i]:
#             people_waiting -= 4 - lift_state[i]
#             lift_state[i] = 4
#         else:
#             lift_state[i] += people_waiting
#             people_waiting = 0
#
# is_not_full = False
#
# for i in range(len(lift_state)):
#     if lift_state[i] < 4:
#         is_not_full = True
#         break
#
# if people_waiting == 0 and is_not_full:
#     print("The lift has empty spots!")
# elif people_waiting > 0 and is_not_full == False:
#     print(f"There isn't enough space! {people_waiting} people in a queue!")
#
# print(*lift_state)
#
#
