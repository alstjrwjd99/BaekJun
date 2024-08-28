def solution(m, musicinfos):
    answer = []

    def seperate_music(m):
        new_m = []
        i = 0
        while i < len(m):
            if i < len(m) - 1 and m[i + 1] == '#':
                new_m.append(m[i] + '#')
                i += 2
            else:
                new_m.append(m[i])
                i += 1
        return new_m
    
    m = seperate_music(m)
    
    for input_time, musicinfo in enumerate(musicinfos):
        start, end, title, music = musicinfo.split(',')
        music = seperate_music(music)
        hour, minute = start.split(':')
        start = int(hour) * 60 + int(minute)
        hour, minute = end.split(':')
        end = int(hour) * 60 + int(minute)
        
        # 음악의 재생시간
        play_time = end - start
        total = []
        for i in range(play_time):
            total.append(music[i % len(music)])
        
        # 재생된 멜로디에서 주어진 멜로디 m을 찾기
        for i in range(len(total) - len(m) + 1):
            if total[i:i + len(m)] == m:
                answer.append((play_time, input_time, title))
                break
    
    if not answer:
        return '(None)'
    
    # 재생 시간이 긴 순서대로, 입력 순서가 이른 순서대로 정렬
    answer.sort(key=lambda x: (-x[0], x[1]))

    return answer[0][2]