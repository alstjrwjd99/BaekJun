def solution(lines):
    answer = set()
    dup = set()
    for line in lines :
        for i in range (line[0],line[1]):
            if i+0.5 in dup:
                answer.add(i+0.5)
            else :
                dup.add(i+0.5)        
    return len(answer)
