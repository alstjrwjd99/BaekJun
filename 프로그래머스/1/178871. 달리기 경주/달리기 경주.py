def solution(players, callings):
    race = {name : i for i, name in enumerate (players) }
    for name in callings:
        idx = race[name]
        race[name] -= 1
        race[players[idx-1]] += 1
        players[idx-1],players[idx] = players[idx],players[idx-1] 
    return players