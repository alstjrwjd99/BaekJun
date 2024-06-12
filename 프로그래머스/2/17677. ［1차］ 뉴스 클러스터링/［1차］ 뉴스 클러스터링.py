'''
1. 문자열 추출 후 소문자로
2. 교집합, 합집합 구하기
'''
from collections import Counter

def solution(str1, str2):
    answer = 0
    str1, str2 = str1.lower(), str2.lower()
    s1 = []
    s2 = []
    total = 0
    for i in range (len(str1)-1):
        if 96 < ord(str1[i]) < 123 and 96 < ord(str1[i+1]) < 123:
            s1.append(str1[i]+str1[i+1])
            total += 1
    for i in range (len(str2)-1):
        if 96 < ord(str2[i]) < 123 and 96 < ord(str2[i+1]) < 123:
            s2.append(str2[i]+str2[i+1])
            total += 1
    c1 = Counter(s1)
    c2 = Counter(s2)
    
    if len(c1) == 0 and len(c2) == 0:
        return 65536

    intersect = 0
    conjunct = 0
    
    # 교집합 구하기
    for alpha in c1 :
        if alpha in c2 and c2[alpha] > 0:
            tmp = min(c1[alpha],c2[alpha])
            intersect += tmp
            c1[alpha] -= tmp
            c2[alpha] -= tmp
    for alpha in c2 :
        if alpha in c1 and c1[alpha] > 0:
            tmp = min(c1[alpha],c2[alpha])
            intersect += tmp
            c1[alpha] -= tmp
            c2[alpha] -= tmp
    
    # 합집합 구하기
    conjunct = total - intersect
    
    answer = int((intersect / conjunct) * 65536)
    return answer