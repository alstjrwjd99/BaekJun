'''
a > b 인 자연수일 때
a*b > (a-1)*(b-1)이 성립
'''
def solution(n, s):
    if n > s:
        return [-1]
    answer = [s//n for _ in range (n)]
    mod = s % n
    for i in range (1, mod+1):
        answer[n-i] += 1
    return answer