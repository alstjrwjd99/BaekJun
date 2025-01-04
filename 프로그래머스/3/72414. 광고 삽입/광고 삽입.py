def solution(play_time, adv_time, logs):
    def change_second(time_str):
        h, m, s = map(int, time_str.split(':'))
        return h * 3600 + m * 60 + s
    
    def change_time(second):
        return f'{second // 3600:02d}:{(second % 3600) // 60:02d}:{second % 60:02d}'
    
    play_time_sec = change_second(play_time)
    adv_time_sec = change_second(adv_time)

    frame = [0] * (play_time_sec + 1)

    for log in logs:
        start, end = map(change_second, log.split('-'))
        frame[start] += 1
        frame[end] -= 1

    for i in range(1, len(frame)):
        frame[i] += frame[i - 1]

    for i in range(1, len(frame)):
        frame[i] += frame[i - 1]

    max_watch_time = 0
    start_time = 0

    for start in range(play_time_sec - adv_time_sec + 1):
        end = start + adv_time_sec
        current_watch_time = frame[end - 1] - (frame[start - 1] if start > 0 else 0)
        
        if current_watch_time > max_watch_time:
            max_watch_time = current_watch_time
            start_time = start

    return change_time(start_time)