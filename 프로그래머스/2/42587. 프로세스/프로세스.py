from collections import deque
def solution(priorities, location):
    answer = 0
    rank = []
    for i,priority in enumerate(priorities):
        rank.append((priority,i)) 
    queue = deque(rank)
    priorities.sort()
    while (queue):
        tmp = queue.popleft()
        if tmp[0] == priorities[-1]:
            priorities.pop()
            answer += 1
            if tmp[1] == location:
                break
        else :
            queue.append(tmp)
    return answer