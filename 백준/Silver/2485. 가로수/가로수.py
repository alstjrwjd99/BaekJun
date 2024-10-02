'''
구해야하는 것 : 두 숫자간 차이들의 최대공약수
결과 : sum(차이값 / 최대공약수 - 1)
'''
import sys
input = sys.stdin.readline

import math

n = int(input())

differ = []
trees = []
for check in range (n):
    tree = int(input())
    if check != 0:
        differ.append(tree - trees[-1])
    trees.append(tree)
    
differ_gcd = math.gcd(*differ)
answer = 0
for i in range (n-1):
    answer += (differ[i] // differ_gcd) - 1
print(answer)