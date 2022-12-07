deck = input().split()
faro_shuffles = int(input())

for current_shuffle in range(faro_shuffles):
    new_deck = []
    middle_in_deck = len(deck) // 2
    left_part = deck[:middle_in_deck]
    right_part = deck[middle_in_deck:]
    for i in range(middle_in_deck):
        new_deck.append(left_part[i])
        new_deck.append(right_part[i])
    deck = new_deck

print(deck)
