def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse = True)
    for key,a in enumerate(A):
        answer += a * B[key]
    return answer