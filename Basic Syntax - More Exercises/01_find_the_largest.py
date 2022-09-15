number = input()

number_list = [str(x) for x in number]
number_list.sort(reverse=True)
print("".join(number_list))
