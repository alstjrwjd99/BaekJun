def solution(routes):
    routes.sort()
    answer = 0
    camera = routes[0]
    for i in routes[1:]:
        # 겹치면 카메라의 범위를 겹치는 범위로 조정
        if i[0]<=camera[1]:
            camera = [i[0], min(i[1], camera[1])]
        # 안 겹치면 카메라 한대 추가
        else:
            camera = i
            answer+=1
    return answer+1
