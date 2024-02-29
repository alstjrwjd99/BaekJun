def solution(friends, gifts):
    lenf = len(friends)
    answer = [0] * lenf
    relation = [[0] * lenf for _ in range (lenf)]
    for index,gift in enumerate (gifts):
        temp = gift.split()
        relation[friends.index(temp[0])][friends.index(temp[1])] += 1
    print(relation)
    index = [[0] * 3 for _ in range (lenf)]
    for a in range (lenf):
        index[a][0] = sum(relation[a])
        for b in range (lenf):
            index[a][1] += relation[b][a]
        index[a][2] = index[a][0] - index[a][1]
    print(index)
    for i in range (lenf):
        for j in range (lenf):
            if relation[i][j] > relation[j][i]:
                answer[i] += 1
            elif relation[i][j] == relation[j][i]:
                if index[i][2] > index[j][2]:
                    answer[i] += 1
    print(answer)
    return max(answer)