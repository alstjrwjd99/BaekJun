'''
브루트 포스
1. 가능한 조합 구하기 n / 2 ex) 1,2 선택
2. 각 조합 별로 주사위의 합의 경우의 수 구하기 ex) 4(합) : 4(경우의 수), 5 : 4...
3. 자신이 선택한 반대 경우와 비교
4. 승이 가장 많은 주사위 선택
'''
from copy import deepcopy
from collections import defaultdict

def solution(dice):
    if len(dice) == 2:
        left, right = 0, 0
        for i in dice[0]:
            for j in dice[1]:
                if i < j:
                    left += 1
                elif i > j:
                    right += 1
        if left > right:
            return [2]
        elif left < right:
            return [1]

    answer = []
    n = len(dice)
    combi = []
    for_extra = set([i for i in range(1, n + 1)])
    all_sum_combi = defaultdict(dict)

    def dfs(made, start):
        if len(made) == n // 2:
            new_made = deepcopy(made)
            temp = defaultdict(int)
            
            for t in dice[new_made[0] - 1]:
                temp[t] += 1
            
            def make_sum_case(prev, curr):
                tmp = defaultdict(int)
                for p, pv_count in prev.items():
                    for c in curr:
                        tmp[p + c] += pv_count
                return tmp

            for m in range(1, len(new_made)):
                temp = make_sum_case(temp, dice[new_made[m] - 1])

            all_sum_combi[f'{new_made}'] = temp
            combi.append(new_made)
            return

        for i in range(start, n + 1):
            made.append(i)
            dfs(made, i + 1)
            made.pop()

    dfs([], 1)
    
    max_win = -1
    for c in combi:
        left, right = 0, 0
        extra = list(for_extra - set(c))
        for key1, value1 in all_sum_combi[f'{c}'].items():
            for key2, value2 in all_sum_combi[f'{extra}'].items():
                if key1 < key2:
                    right += value1 * value2
                elif key1 > key2:
                    left += value1 * value2
        if max_win < left :
            answer = c
            max_win = left

    return answer