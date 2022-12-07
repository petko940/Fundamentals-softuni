def player_info(player, position, skill, players_data: dict):
    if player not in players_data:
        players_data[player] = {position: skill}
    if position not in players_data[player]:
        players_data[player][position] = skill
    if skill > players_data[player][position]:
        players_data[player][position] = skill


def pvp(player1, player2, players_data: dict):
    if player1 in players_data and player2 in players_data:
        p1_sum = sum(players_data[player1].values())
        p2_sum = sum(players_data[player2].values())
        for x in players_data[player1].keys():
            if x in players_data[player2].keys():
                if p1_sum > p2_sum:
                    players_data.pop(player2)
                elif p1_sum < p2_sum:
                    players_data.pop(player1)
                break


players_data = {}
best_player = []
commands = input()
while "Season end" not in commands:
    if "->" in commands:
        player, position, skill = [int(x) if x.isdigit() else x for x in commands.split(" -> ")]
        player_info(player, position, skill, players_data)
    elif "vs" in commands:
        player1, player2 = commands.split(" vs ")
        pvp(player1, player2, players_data)
    commands = input()


for player_name in players_data:
    best_player.append({"player_name": player_name, "total_score": sum(players_data[player_name].values())})

for key in sorted(best_player, key=lambda x: (-x["total_score"], x["player_name"])):
    print(f"{key['player_name']}: {key['total_score']} skill")
    for position, skill in sorted(players_data[key['player_name']].items(), key=lambda x: (-x[1], x[0])):
        print(f"- {position} <::> {skill}")
