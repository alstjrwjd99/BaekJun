from collections import deque
def solution(n, computers):
    answer = 0
    queue = deque([])
    connected = set()
    for i in range (n):
        visited = set()
        if i not in connected:
            queue.append(i)
            visited.add(i)
        while queue:
            node = queue.popleft()
            # print('시작 node : ',computers[node])
            for idx, network in enumerate (computers[node]):
                # print(network)
                if idx not in connected and idx not in visited and network == 1:
                    # print('queue에 담길 idx : ',  idx)
                    queue.append(idx)
                    visited.add(idx)
        for a in visited:
            connected.add(a)
        if len(visited) != 0:
            answer += 1
        # print(connected)
    return answer
