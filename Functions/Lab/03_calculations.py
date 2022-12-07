def operator_func(event, a, b):
    if event == "multiply":
        return a * b
    elif event == "divide":
        return a // b
    elif event == "add":
        return a + b
    elif event == "subtract":
        return a - b


print(operator_func(input(), int(input()), int(input())))
