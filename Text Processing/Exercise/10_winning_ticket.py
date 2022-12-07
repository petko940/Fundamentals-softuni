def check_ticket(ticket):
    if len(ticket) == 20:
        symbols = ['@', '#', '$', '^']
        left_part = ticket[:10]
        right_part = ticket[10:]
        for symbol in symbols:
            for x in range(10, 5, -1):
                if symbol * x in left_part and symbol * x in right_part:
                    if x == 10:
                        return f'ticket "{ticket}" - {x}{symbol} Jackpot!'
                    else:
                        return f'ticket "{ticket}" - {x}{symbol}'
        return f'ticket "{ticket}" - no match'
    return "invalid ticket"


def main():
    tickets = [x.strip() for x in input().split(",")]
    for ticket in tickets:
        print(check_ticket(ticket))


if __name__ == "__main__":
    main()
