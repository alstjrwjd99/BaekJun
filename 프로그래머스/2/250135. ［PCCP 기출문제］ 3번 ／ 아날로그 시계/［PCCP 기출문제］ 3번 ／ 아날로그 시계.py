'''
초침과 분침, 초침과 시침이 겹칠때 알람이 울림

1초에 움직이는 각도
초침 : 6도 
분침 : 1/10도
시침 : 1/120도
'''
def solution(h1, m1, s1, h2, m2, s2):
    # 시작 시간을 초로 변환
    start = to_second(h1, m1, s1)
    # 끝나는 시간을 초로 변환
    end = to_second(h2, m2, s2)

    # 끝나는 시간까지 겹친 횟수에서 시작 시간까지 겹친 횟수를 빼고, 
    # 시작 시간에 울리는지 확인하여 더한다
    answer = cal(end) - cal(start) + (1 if alram_now(start) else 0)
    
    return answer

def cal(time):
    # 초침과 분침이 겹치는 횟수 계산
    sm = time * 59 // 3600  # 초침과 분침은 59번 겹친다 (3600초 동안)
    
    # 초침과 시침이 겹치는 횟수 계산
    sh = time * 719 // 43200  # 초침과 시침은 43200초 동안 719번 겹친다
    
    # 12:00:00에서 시침과 분침이 겹치는 경우를 제외
    a = 2 if time >= 43200 else 1
    
    return sm + sh - a

def to_second(h, m, s):
    # 시, 분, 초를 초로 변환
    return h * 3600 + m * 60 + s

def alram_now(time):
    # 현재 시간에서 초침과 분침, 초침과 시침이 겹치는지 확인
    return (time * 59 % 3600 == 0) or (time * 719 % 43200 == 0)