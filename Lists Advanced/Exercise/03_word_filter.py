words = [x for x in input().split()]

new_words = [print(x) for x in words if len(x) % 2 == 0]
