string = input()

while string != "End":
    chars = list(string)
    if string == "SoftUni":
        string = input()
        continue
    output = [i*2 for i in chars]
    print("".join(output))
    string = input()
