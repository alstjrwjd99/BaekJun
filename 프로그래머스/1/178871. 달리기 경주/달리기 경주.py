def solution(players, callings):
    answer = []
    ranking = {player : idx for idx,player in enumerate(players)}

    for call in callings:
        rank = ranking[call]
        lose_player = players[rank-1]
        players[rank-1], players[rank] = players[rank], players[rank-1]
        ranking[call] -= 1
        ranking[lose_player] += 1 
    for name, rank in sorted(list(ranking.items()),key=lambda x : x[1]):
        answer.append(name)

    return answer