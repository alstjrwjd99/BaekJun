from collections import deque

def solution(game_board, table):
    answer = 0
    n = len(game_board)
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def in_range(x, y):
        return 0 <= x < n and 0 <= y < n

    def bfs(board, start_x, start_y, find_value):
        queue = deque([(start_x, start_y)])
        block = []
        board[start_x][start_y] = find_value ^ 1  # 방문 처리 (0은 1로, 1은 0으로 변경)
        while queue:
            x, y = queue.popleft()
            block.append((x - start_x, y - start_y))  # 상대 좌표 저장
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if in_range(nx, ny) and board[nx][ny] == find_value:
                    board[nx][ny] = find_value ^ 1
                    queue.append((nx, ny))
        return block

    def rotate(block):
        return [(-y, x) for x, y in block]

    def normalize(block):
        min_x = min(x for x, y in block)
        min_y = min(y for x, y in block)
        return sorted((x - min_x, y - min_y) for x, y in block)

    def get_rotations(block):
        rotations = []
        for _ in range(4):
            block = rotate(block)
            normalized_block = normalize(block)
            if normalized_block not in rotations:
                rotations.append(normalized_block)
        return rotations

    def find_blocks(board, value):
        blocks = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == value:
                    block = bfs(board, i, j, value)
                    blocks.append(normalize(block))
        return blocks

    # 게임보드에서 구멍(0) 찾기
    goal_holes = find_blocks(game_board, 0)
    # 테이블에서 블록(1) 찾기
    have_blocks = find_blocks(table, 1)

    for hole in goal_holes:
        hole_rotations = get_rotations(hole)
        for block in have_blocks:
            block_rotations = get_rotations(block)
            if any(h in block_rotations for h in hole_rotations):
                answer += len(block)
                have_blocks.remove(block)
                break

    return answer