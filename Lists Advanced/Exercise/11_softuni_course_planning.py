def add(new_lesson, list_: list):
    if new_lesson not in list_:
        list_.append(new_lesson)


def insert(new_lesson, index_, list_: list):
    if new_lesson not in list_:
        list_.insert(index_, new_lesson)


def remove(new_lesson, list_: list):
    if new_lesson in list_:
        list_.remove(new_lesson)
        if f"{new_lesson}-Exercise" in list_:
            list_.remove(f"{new_lesson}-Exercise")


def swap(lesson_one, lesson_two, list_: list):
    if lesson_one in list_ and lesson_two in list_:
        index_lesson_one = list_.index(lesson_one)
        index_lesson_two = list_.index(lesson_two)
        list_[index_lesson_one], list_[index_lesson_two] = list_[index_lesson_two], list_[index_lesson_one]
        if f"{lesson_one}-Exercise" in list_:
            list_.pop(index_lesson_one + 1)
            list_.insert(index_lesson_two + 1, f"{list_[index_lesson_two]}-Exercise")
        elif f"{lesson_two}-Exercise" in list_:
            list_.pop(index_lesson_two + 1)
            list_.insert(index_lesson_one + 1, f"{list_[index_lesson_one]}-Exercise")


def exercise(new_lesson, new_lesson_exercise, list_: list):
    if new_lesson not in list_ and new_lesson_exercise not in list_:
        list_.append(new_lesson)
        list_.append(new_lesson_exercise)
    elif new_lesson in list_ and new_lesson_exercise not in list_:
        index_ = list_.index(new_lesson)
        list_.insert(index_ + 1, f"{new_lesson}-Exercise")


schedule = input().split(", ")

command = input()
while "course start" not in command:
    command = command.split(":")
    if "Add" in command:
        lesson = command[1]
        add(lesson, schedule)
    elif "Insert" in command:
        lesson = command[1]
        index = int(command[2])
        insert(lesson, index, schedule)
    elif "Remove" in command:
        lesson = command[1]
        remove(lesson, schedule)
    elif "Swap" in command:
        lesson1 = command[1]
        lesson2 = command[2]
        swap(lesson1, lesson2, schedule)
    elif "Exercise" in command:
        lesson = command[1]
        lesson_exercise = f"{lesson}-Exercise"
        exercise(lesson, lesson_exercise, schedule)
    command = input()

for number in range(len(schedule)):
    print(f"{number + 1}.{schedule[number]}")
