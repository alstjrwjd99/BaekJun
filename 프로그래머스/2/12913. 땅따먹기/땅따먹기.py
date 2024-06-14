# dp
def solution(land):
    for i in range (1,len(land)):
        for j in range(4):
            tmp = 0
            for k in range (4):
                if j == k:
                    continue
                if tmp < land[i-1][k]:
                    tmp = land[i-1][k]
            land[i][j] += tmp
    return max(land[-1])