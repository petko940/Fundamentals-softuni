def add_people(people: int):
    train[-1] += people


def insert_people(index, people):
    train[index] += people


def leave_people(index, people):
    left_people = train[index] - people
    train[index] = left_people


wagons = int(input())
train = [0] * wagons
command = input().split()

while command[0] != "End":
    if command[0] == "add":
        add_people(int(command[1]))
    elif command[0] == "insert":
        indx = int(command[1])
        number = int(command[2])
        insert_people(indx, number)
    elif command[0] == "leave":
        indx = int(command[1])
        number = int(command[2])
        leave_people(indx, number)
    command = input().split()

print(train)
