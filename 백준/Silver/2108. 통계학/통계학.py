from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
numbers = [
    int(input().strip())
    for _ in range (n)
]

print(round(sum(numbers)/n))
numbers.sort()
print(numbers[n//2])
c = Counter(numbers).most_common(2)
if len(c) == 2 and c[0][1] == c[1][1] :
    print(c[1][0])
else :
    print(c[0][0])
print(numbers[-1] - numbers[0])