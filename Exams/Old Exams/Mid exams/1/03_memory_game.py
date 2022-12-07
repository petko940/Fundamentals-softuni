def cheat(count_func, list_):
    middle = len(list_) // 2
    list_.insert(middle, f"-{count_func}a")
    list_.insert(middle, f"-{count_func}a")
    return "Invalid input! Adding additional elements to the board"


def match_elements(idx1, idx2, list_):
    element_from_list = list_.pop(idx1)
    list_.pop(idx2 - 1)
    return f"Congrats! You have found matching elements - {element_from_list}!"


sequence_of_elements = input().split()
command = input()
count = 0
while "end" not in command:
    command = command.split()
    index1 = int(command[0])
    index2 = int(command[1])
    count += 1
    if index1 > index2:
        index1, index2 = index2, index1

    if not (0 <= index1 < len(sequence_of_elements)
            and 0 <= index2 < len(sequence_of_elements)) \
            or index1 == index2:
        print(cheat(count, sequence_of_elements))
    else:
        if sequence_of_elements[index1] == sequence_of_elements[index2]:
            print(match_elements(index1, index2, sequence_of_elements))
        else:
            print("Try again!")

    if not len(sequence_of_elements):
        print(f"You have won in {count} turns!")
        break
    command = input()
else:
    print("Sorry you lose :(")
    print(*sequence_of_elements)
