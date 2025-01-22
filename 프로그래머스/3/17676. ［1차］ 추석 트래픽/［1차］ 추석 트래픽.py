def solution(lines):
    answer = 0
    intervals = []

    def time_to_milliseconds(h, m, s):
        sec, millisec = map(int, s.split('.'))
        return (h * 3600 + m * 60 + sec) * 1000 + millisec

    for line in lines:
        date, time, duration = line.split()
        h, m, s = time.split(':')
        duration = float(duration[:-1]) * 1000
        end_time = time_to_milliseconds(int(h), int(m), s)
        start_time = end_time - int(duration) + 1
        intervals.append((start_time, end_time))

    for start, end in intervals:
        count = 0
        start_range = start
        end_range = start + 999  

        for s, e in intervals:
            if s <= end_range and e >= start_range:
                count += 1
        answer = max(answer, count)

        count = 0
        start_range = end
        end_range = end + 999 
        
        for s, e in intervals:
            if s <= end_range and e >= start_range:
                count += 1
        answer = max(answer, count)

    return answer