def solution(schedules, timelogs, startday):
    answer = 0
    
    def time_to_minute(s):
        return s // 100 * 60 + s % 100
    
    for person, schedule in enumerate(schedules):
        all_attend = True
        for date, log in enumerate(timelogs[person]):
            if ((date + startday) % 7 == 0 or (date + startday) % 7 == 6) : 
                continue
            if (time_to_minute(schedule) + 10 < time_to_minute(log)) : 
                all_attend = False
                break
        if all_attend :
            answer += 1
    return answer