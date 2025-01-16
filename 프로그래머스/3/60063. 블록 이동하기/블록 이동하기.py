from collections import deque

def solution(board):
    n = len(board)
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    queue = deque([(0, 0, 0, 1, 0)])  # x1, y1, x2, y2, cnt
    visited = set([(0, 0, 0, 1)])  # 로봇 상태 저장

    def in_range(x, y):
        return 0 <= x < n and 0 <= y < n

    while queue:
        x1, y1, x2, y2, cnt = queue.popleft()
        if (x1, y1) == (n-1, n-1) or (x2, y2) == (n-1, n-1):
            return cnt

        # 4방향 직진
        for i in range(4):
            nx1, ny1 = x1 + dx[i], y1 + dy[i]
            nx2, ny2 = x2 + dx[i], y2 + dy[i]
            if in_range(nx1, ny1) and in_range(nx2, ny2):
                if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
                    if (nx1, ny1, nx2, ny2) not in visited:
                        queue.append((nx1, ny1, nx2, ny2, cnt + 1))
                        visited.add((nx1, ny1, nx2, ny2))

        # 회전 (가로 상태)
        if x1 == x2:  # 가로로 놓여 있는 경우
            for d in [-1, 1]:  # 위(-1), 아래(+1) 방향 회전
                if in_range(x1 + d, y1) and in_range(x2 + d, y2):
                    if board[x1 + d][y1] == 0 and board[x2 + d][y2] == 0:
                        # 첫 번째 축 회전
                        if (x1, y1, x1 + d, y1) not in visited:
                            queue.append((x1, y1, x1 + d, y1, cnt + 1))
                            visited.add((x1, y1, x1 + d, y1))
                        # 두 번째 축 회전
                        if (x2, y2, x2 + d, y2) not in visited:
                            queue.append((x2, y2, x2 + d, y2, cnt + 1))
                            visited.add((x2, y2, x2 + d, y2))

        # 회전 (세로 상태)
        if y1 == y2:  # 세로로 놓여 있는 경우
            for d in [-1, 1]:  # 왼쪽(-1), 오른쪽(+1) 방향 회전
                if in_range(x1, y1 + d) and in_range(x2, y2 + d):
                    if board[x1][y1 + d] == 0 and board[x2][y2 + d] == 0:
                        # 첫 번째 축 회전
                        if (x1, y1, x1, y1 + d) not in visited:
                            queue.append((x1, y1, x1, y1 + d, cnt + 1))
                            visited.add((x1, y1, x1, y1 + d))
                        # 두 번째 축 회전
                        if (x2, y2, x2, y2 + d) not in visited:
                            queue.append((x2, y2, x2, y2 + d, cnt + 1))
                            visited.add((x2, y2, x2, y2 + d))

    return -1