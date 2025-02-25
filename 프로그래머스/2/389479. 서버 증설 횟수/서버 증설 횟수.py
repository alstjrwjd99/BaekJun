'''
m = 3
3명 이상 -> 1대
6명 이상 -> 2대

k시간 동안 유지 -> queue로 담아서 처리

현재 증설된 서버의 수로 player를 커버할 수 없으면 서버 증설
필요한 서버의 수 : player // m 
증설횟수 -> answer += 필요한 서버의 수 - 이전에 증설되어 있던 서버의 수
'''
from collections import deque

def solution(players, m, k):
    answer = 0
    queue = deque()
    server_cnt = 0
    
    for time, player in enumerate(players):
        if queue and queue[0][0] + k == time :
            old_time, old_server_cnt = queue.popleft()
            server_cnt -= old_server_cnt
        
        need_server_cnt = player // m
        if player >= m and server_cnt <= need_server_cnt:
            answer += (need_server_cnt - server_cnt)
            queue.append((time, need_server_cnt - server_cnt))
            server_cnt = need_server_cnt
            
    return answer