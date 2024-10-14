def solution(citations):
    n = len(citations)
    while True and n > 0:
        if sum([x >= n for x in citations]) >= n:
            break
        else:
            n -= 1
    return n