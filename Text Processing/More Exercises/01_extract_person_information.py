n = int(input())

for _ in range(n):
    random_text = input()
    name_age = random_text.split()
    # name,age = "",""
    for x in name_age:
        if "@" in x:
            start_index = x.index("@")
            end_index = x.index("|")
            name = x[start_index + 1:end_index]
        if "#" in x:
            start_index = x.index("#")
            end_index = x.index("*")
            age = x[start_index + 1:end_index]
    print(f"{name} is {age} years old.")
