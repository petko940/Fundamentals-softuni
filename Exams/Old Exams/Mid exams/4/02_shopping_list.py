def is_exists(item_, list_with_groceries_):
    if item_ in list_with_groceries_:
        return True


def urgent(item_, list_with_groceries_):
    if not is_exists(item_, list_with_groceries_):
        list_with_groceries_.insert(0, item_)


def unnecessary(item_, list_with_groceries_):
    if is_exists(item_, list_with_groceries):
        list_with_groceries_.remove(item_)


def correct(item_, new_item_, list_with_groceries_):
    if is_exists(item_, list_with_groceries_):
        index = list_with_groceries_.index(item_)
        list_with_groceries_[index] = new_item_


def rearrange(item_, list_with_groceries_):
    if is_exists(item_, list_with_groceries_):
        index = list_with_groceries_.index(item_)
        list_with_groceries_.append(list_with_groceries_.pop(index))


list_with_groceries = input().split("!")
command = input()

while "Go Shopping!" not in command:
    command = command.split()
    if "Urgent" in command:
        item = command[1]
        urgent(item, list_with_groceries)
    elif "Unnecessary" in command:
        item = command[1]
        unnecessary(item, list_with_groceries)
    elif "Correct" in command:
        old_item = command[1]
        new_item = command[2]
        correct(old_item, new_item, list_with_groceries)
    elif "Rearrange" in command:
        item = command[1]
        rearrange(item, list_with_groceries)
    command = input()

print(", ".join(list_with_groceries))
