from collections import defaultdict

def solution(points, routes):
    answer = 0
    robot_route_list = []

    # 포인트 좌표 딕셔너리 생성
    point_dict = {i + 1: points[i] for i in range(len(points))}

    # 각 로봇의 경로 생성
    for route in routes:
        robot_route = []
        start = point_dict[route[0]][:]  # 시작 좌표 복사

        for j in range(1, len(route)):
            end = point_dict[route[j]]

            # X축 이동
            while start[0] != end[0]:
                robot_route.append(tuple(start))
                if end[0] > start[0]:
                    start[0] += 1
                else:
                    start[0] -= 1

            # Y축 이동
            while start[1] != end[1]:
                robot_route.append(tuple(start))
                if end[1] > start[1]:
                    start[1] += 1
                else:
                    start[1] -= 1

        # 마지막 위치 추가
        robot_route.append(tuple(start))
        robot_route_list.append(robot_route)

    # 충돌 확인을 위한 경로 처리
    while any(robot_route_list):
        current_positions = set()  # 현재 시간대에 있는 로봇 좌표
        danger_positions = set()  # 위험 좌표 (중복된 좌표)
        
        for robot_route in robot_route_list:
            if robot_route:
                position = robot_route.pop(0)
                if position in current_positions and position not in danger_positions:
                    answer += 1
                    danger_positions.add(position)  # 위험 위치 추가
                current_positions.add(position)

    return answer