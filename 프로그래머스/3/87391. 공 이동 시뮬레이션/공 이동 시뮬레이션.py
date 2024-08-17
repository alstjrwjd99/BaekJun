def solution(n, m, goal_x, goal_y, queries):
    # 초기화
    min_x, max_x = goal_x, goal_x
    min_y, max_y = goal_y, goal_y
    
    reverse_directions = [(0,1),(0,-1),(1,0),(-1,0)]
    
    for command, length in reversed(queries):
        dx, dy = reverse_directions[command]
        
        # X 방향으로 이동
        if dx != 0:
            if dx == 1:  # 아래로 이동
                max_x = min(n - 1, max_x + length)
                if min_x > 0:
                    min_x += length
            elif dx == -1:  # 위로 이동
                min_x = max(0, min_x - length)
                if max_x < n - 1:
                    max_x -= length
        
        # Y 방향으로 이동
        if dy != 0:
            if dy == 1:  # 오른쪽으로 이동
                max_y = min(m - 1, max_y + length)
                if min_y > 0:
                    min_y += length
            elif dy == -1:  # 왼쪽으로 이동
                min_y = max(0, min_y - length)
                if max_y < m - 1:
                    max_y -= length
        
        # 범위를 벗어나면 목표 지점에 도달할 수 없음
        if min_x >= n or max_x < 0 or min_y >= m or max_y < 0:
            return 0
    
    # 가능한 위치 개수를 반환
    return (max_x - min_x + 1) * (max_y - min_y + 1)