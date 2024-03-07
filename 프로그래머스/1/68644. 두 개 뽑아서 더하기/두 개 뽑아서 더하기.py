from itertools import combinations
def solution(numbers):
    answer = []
    tmp = set()
    for i in (list(combinations(numbers,2))):
        tmp.add(sum(i))
    answer = list(tmp)
    answer.sort()
    return answer