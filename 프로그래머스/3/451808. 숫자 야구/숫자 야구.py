'''
1. 만들 수 있는 숫자를 다 만들기 10P4 -> 10 * 9 * 8 * 7 = 5040
2. 각 guess 후보에 대해 이 guess가 strike/ball 결과를 얼마나 고르게 분할하나를 엔트로피(정보이득) 로 계산
3. 가장 엔트로피가 높은 후보를 다음 시도로 선택
4. 실제 결과에 맞는 후보만 남기고 반복
'''
from itertools import permutations

def compare(a, b):
    s = sum(x == y for x, y in zip(a, b))
    b = sum(x in b for x in a) - s
    return s, b

def best_guess(candidates):
    # 후보가 적으면 그냥 아무거나
    if len(candidates) <= 2:
        return candidates[0]

    best_score = float('inf')
    best = None
    
    # 각 guess가 후보를 얼마나 고르게 분할하나 측정
    for g in candidates[:150]:  # 전부 돌리면 느림 -> 상위 일부만 샘플링
        partitions = {}
        for c in candidates:
            res = compare(g, c)
            partitions[res] = partitions.get(res, 0) + 1
        # 최대 그룹 크기(편향도)를 최소화하는 guess 선택
        score = max(partitions.values())
        if score < best_score:
            best_score = score
            best = g
    return best

def solution(n, submit):
    candidates = [''.join(p) for p in permutations('123456789', 4)]

    while candidates:
        guess = best_guess(candidates)
        res = submit(int(guess))
        s, b = map(int, res.replace('S', '').replace('B', '').split())
        if s == 4:
            return int(guess)
        candidates = [c for c in candidates if compare(c, guess) == (s, b)]
        if len(candidates) == 1:
            return int(candidates[0])
    return int(candidates[0])