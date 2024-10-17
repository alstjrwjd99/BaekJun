from collections import Counter

def solution(want, number, discount):
    answer = 0
    window = sum(number)
    for i in range (len(discount) - window +1):
        c = Counter(discount[i:i+window])
        can_buy = True
        for idx,w in enumerate(want):
            if c[w] != number[idx] : can_buy = False
        if can_buy : answer += 1
    return answer