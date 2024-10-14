from functools import cmp_to_key

def solution(numbers):
    def compare(a, b):
        a, b = str(a), str(b)
        if a + b > b + a:
            return -1
        elif a + b < b + a:
            return 1
        else:
            return 0
    numbers.sort(key=cmp_to_key(compare))
    return str(int(''.join(map(str, numbers))))