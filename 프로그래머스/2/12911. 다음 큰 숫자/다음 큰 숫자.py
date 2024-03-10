def solution(n):
    answer = 0
    binary = bin(n)
    one = binary.count('1')
    while True:
        n += 1
        bina = bin(n)
        other = bina.count('1')
        if one == other:
            answer = n
            break
    return answer