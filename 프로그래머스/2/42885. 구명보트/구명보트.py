def solution(people, limit):
    answer = 0
    i = 0
    N = len(people) - 1
    people.sort()
    while (i <= N) :
        if people[i] + people[N] <= limit :
            i += 1
        answer += 1
        N -= 1 
    return (answer)