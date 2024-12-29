from collections import deque

def solution(n, t, m, timetable):
    answer = ''
    bus_depart_time_table = get_bus_depart_time_table(n,t)
    minute_table = sorted([ change_time_to_minute(t) for t in timetable])
    queue = deque(minute_table)  
    last_time = []
    for idx, bus_time in enumerate(bus_depart_time_table):
        cnt = m
        while queue and queue[0] <= bus_time and cnt > 0:
            a = queue.popleft()
            if idx == n - 1 :
                last_time.append(a)
            cnt -= 1
    # 콘이 막차를 탈 수 있는 경우
    if len(last_time) < m :
        answer = change_minute_to_time(bus_time)
    else :
        answer = change_minute_to_time(last_time[-1]-1)
    return answer

# 버스가 출발하는 시간을 구하는 함수
def get_bus_depart_time_table(n, t):
    time_table = [540]
    for i in range (n-1):
        time_table.append(540 + (i+1) * int(t))
    return time_table

def change_time_to_minute(time):
    tmp = time.split(':')
    return int(tmp[0]) * 60 + int(tmp[1])

def change_minute_to_time(minute):
    h,m = minute // 60 , minute % 60
    return f'{h:02d}:{m:02d}'

