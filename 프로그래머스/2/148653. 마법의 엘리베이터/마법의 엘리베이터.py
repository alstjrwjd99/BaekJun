def solution(storey):
    answer = 0
    while storey != 0:
        n = storey % 10 

        if n >= 6:
            storey += 10 - n
            answer += 10 - n

        elif n == 5 and (storey // 10) % 10 >= 5:
            storey += 10 - n
            answer += 10 - n

        else:
            answer += n
        storey = storey // 10


    return answer