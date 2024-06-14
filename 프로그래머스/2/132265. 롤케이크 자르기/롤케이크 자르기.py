'''
Counter 써서 왼쪽 오른쪽을 구한다음
for문 돌면서 해당하는 토핑의 숫자만 빼서 비교하기
'''
from collections import Counter

def solution(topping):
    answer = 0
    c = Counter(topping)
    kind = len(c)
    left = set()
    for t in topping:
        left.add(t)
        if c[t] > 1 :
            c[t] -= 1
        elif c[t] == 1:
            c[t] -= 1
            kind -= 1
        if len(left) == kind:
            answer += 1
        
    return answer
