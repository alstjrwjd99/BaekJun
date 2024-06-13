from collections import deque
def solution(k, dungeons):
    answer = -1
    queue = deque([])
    for i,dungeon in enumerate(dungeons):
        visited = set()
        if dungeon[0] <= k:
            visited.add(i)
            queue.append((dungeon,k,1,visited))
        while queue:
            dungeon,cur_fati,cnt,each_visited = queue.popleft()
            after_fati = cur_fati - dungeon[1]
            for j,dun in enumerate(dungeons):
                if after_fati >= dun[0] and j not in each_visited:
                    copy_visited = each_visited.copy()
                    copy_visited.add(j)
                    queue.append((dun,after_fati,cnt+1,copy_visited))
                    answer = max(answer,cnt + 1)
    return answer