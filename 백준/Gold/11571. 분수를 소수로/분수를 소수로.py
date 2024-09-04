import sys
input = sys.stdin.readline

def divide(num1, num2):
    used = {}
    q = ''
    
    integer_part = num1 // num2
    num1 %= num2
    
    if num1 == 0:
        return str(integer_part) + '.(0)'

    q += str(integer_part) + '.'
    
    index = len(q)  # 소수점 이후 첫 자리의 인덱스
    
    while num1 != 0:
        if num1 in used:
            idx = used[num1]
            q = q[:idx] + '(' + q[idx:] + ')'
            break
        
        used[num1] = index
        num1 *= 10
        q += str(num1 // num2)
        num1 %= num2
        index += 1

    if num1 == 0:
        return q + '(0)'
    return q

n = int(input())

for _ in range(n):
    mother, baby = map(int, input().split())
    print(divide(mother, baby))