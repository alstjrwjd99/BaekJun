def solution(n, arr1, arr2):
    answer = []
    for i in range (n):
        secret = arr1[i] | arr2[i]
        maps = ''
        while secret != 0:
            if secret % 2 == 0:
                maps += ' '
            else :
                maps += '#'
            secret //= 2
        maps = maps.ljust(n)
        maps = maps[::-1]
        answer.append(maps)
    return answer