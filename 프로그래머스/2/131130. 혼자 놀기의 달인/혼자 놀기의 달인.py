def solution(cards):
    answer = []
    cards = [0] + cards
    visited = set([0])
    
    def find_cycle(num):
        visited.add(num)
        tmp = []
        while num not in tmp:
            visited.add(cards[num])
            tmp.append(num)
            num = cards[num]
        return tmp
    
    for i in range (1,len(cards)):
        if i not in visited:
            answer.append(find_cycle(i))
            
    if len(answer) == 1: return 0
    answer.sort(key = lambda x : -len(x))
    return len(answer[0]) * len(answer[1])