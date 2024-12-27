from functools import cmp_to_key
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = [input().strip() for _ in range(n)]
max_num = str(max(map(int,numbers)))

for _ in range (m-n):
    numbers.append(max_num)

def compare(x, y):
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    else:
        return 0
    
numbers.sort(key=cmp_to_key(compare))
one_used = int(''.join(numbers))

print(str(one_used))