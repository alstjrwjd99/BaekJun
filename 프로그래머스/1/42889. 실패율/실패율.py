def solution(N, stages):
    answer = []
    user = len(stages)
    clear = {i : 0 for i in range (1,N+1)}
    for i in range (1,N+1):
        if user == 0:
            break
        unclear = stages.count(i)
        clear[i] = unclear / user
        user -= unclear
    sorted_clear = sorted(clear.items(), key=lambda x: x[1], reverse=True)
    answer = [x[0] for x in sorted_clear]
    return answer