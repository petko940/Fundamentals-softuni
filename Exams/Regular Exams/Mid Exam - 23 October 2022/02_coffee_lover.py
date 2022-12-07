data = [x for x in input().split()]
number_commands = int(input())

for _ in range(number_commands):
    command = input().split()
    if "Include" in command:
        coffee = command[1]
        data.append(coffee)
    elif "Remove" in command:
        number_coffees = int(command[2])
        if 0 <= number_coffees < len(data):
            index = int(command[2])
            if command[1] == "first":
                data = data[index:]
            elif command[1] == "last":
                index = -index
                data = data[:index]
    elif "Prefer" in command:
        index1, index2 = [int(x) for x in command if x.isdigit()]
        if 0 <= index1 < len(data) and 0 <= index2 < len(data):
            data[index1], data[index2] = data[index2], data[index1]
    elif "Reverse" in command:
        data.reverse()

print("Coffees:")
print(*data)
