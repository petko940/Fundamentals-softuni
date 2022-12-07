def loading_bar(number):
    number = number // 10
    ready = "%" * number
    not_ready = "." * (10 - number)
    bar = [ready + not_ready]
    bar = str(bar).replace("'", "")
    return bar


num = int(input())
if num == 100:
    print(f"{num}% Complete!\n{loading_bar(num)}")
else:
    print(f"{num}% {loading_bar(num)}\nStill loading...")
