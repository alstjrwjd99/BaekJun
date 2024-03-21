def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    n=len(citations)
    for i in range(n):
        if citations[i]<i+1:
            return i
    return n