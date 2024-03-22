def solution(n, words):
    answer = [0,0]
    game = len(words)
    dup = set()
    dup.add(words[0])
    for i in range (1,game):
        # 이전에 말한 단어 말하는 경우
        if words[i] not in dup:
            dup.add(words[i])
        else :
            return [(i%n)+1, (i//n)+1]
        # 앞의 단어 마지막 글자로 시작하지 않는 경우
        if words[i-1][-1] != words[i][0] :
            return [(i%n)+1, (i//n)+1]    
    return answer