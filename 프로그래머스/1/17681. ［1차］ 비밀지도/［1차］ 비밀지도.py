def solution(n, arr1, arr2):
    answer = []
    for i in range (n):
        secret = arr1[i] | arr2[i]
        maps = bin(secret)
        maps = maps[2:]
        maps = maps.rjust(n,'0')
        maps = maps.replace('1','#')
        maps = maps.replace('0',' ')
        answer.append(maps)
    return answer