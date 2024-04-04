def solution(dots):
    answer = 0
    combination = [(0,1,2,3),(0,2,1,3),(0,3,1,2)]
    for com in combination:
        dx = dots[com[0]][0] - dots[com[1]][0]
        dy = dots[com[0]][1] - dots[com[1]][1]

        nx = dots[com[2]][0] - dots[com[3]][0]
        ny = dots[com[2]][1] - dots[com[3]][1]
        if (dx / nx == dy / ny):

            return 1

    return answer

