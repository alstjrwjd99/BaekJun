import math
from functools import reduce

def solution(arrayA, arrayB):
    answer = 0
    gcdA = reduce(math.gcd, arrayA)
    gcdB = reduce(math.gcd, arrayB)
    
    if gcdA != 1:
        if all(b % gcdA !=0 for b in arrayB) and gcdA >= answer: answer = gcdA

    if gcdB != 1:
        if all(a % gcdB !=0 for a in arrayA) and gcdB >= answer: answer = gcdB

    return answer
