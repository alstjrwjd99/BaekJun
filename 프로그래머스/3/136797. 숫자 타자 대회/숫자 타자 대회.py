from collections import defaultdict

MAX = float('inf')
move_weight = [[-1]*10 for _ in range(10)]

num_coord = lambda x : ( (x-1) % 3, (x-1) // 3 ) if x != 0 else (1, 3)

def weight_cal(ix, iy, jx, jy) :
    if abs(ix - jx) == abs(iy - jy) :
        return 3 * abs(ix - jx) # 대각선방향
    if abs(ix - jx) == 0 :
        return 2 * abs(iy - jy) # 직선방향
    if abs(iy - jy) == 0 :
        return 2 * abs(ix - jx)
    # 혼합
    d_mv = max(abs(ix - jx), abs(iy - jy))
    return 3 + 2 * (d_mv - 1)

def find_move_weight():
    for i in range(10) :
        move_weight[i][i] = 1
        ix, iy = num_coord(i) 
        for j in range(i+1, 10) :
            jx, jy = num_coord(j)
            weight = weight_cal(ix, iy, jx, jy)
            move_weight[i][j] = move_weight[j][i] = weight   
            
def solution(numbers):
    find_move_weight()   
    length = len(numbers)

    num_dict = {(4, 6) : 0}
    
    for num in numbers :
        num = int(num)
        next_dict = defaultdict(lambda : MAX)
        for (lnum, rnum), weight in num_dict.items() :
            if lnum == num or rnum == num :
                next_dict[(lnum, rnum)] = min(next_dict[(lnum, rnum)], weight+1)
                continue
            lweight, rweight = move_weight[lnum][num], move_weight[rnum][num]
            for _weight, _num in [(lweight, rnum), (rweight, lnum)] :
                anum, bnum = (_num, num) if _num < num else (num, _num)
                next_dict[(anum, bnum)] = min(next_dict[(anum, bnum)], weight+_weight)

        num_dict = next_dict

    return min(num_dict.values())