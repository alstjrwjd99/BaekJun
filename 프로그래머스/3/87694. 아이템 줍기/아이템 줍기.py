from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 102 x 102 grid, scaled up to handle half-units
    grid = [[0] * 102 for _ in range(102)]
    
    # Fill the grid according to the rectangles, scaling by 2 for precision
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2
        for row in range(x1, x2 + 1):
            for col in range(y1, y2 + 1):
                grid[row][col] = 1
    
    # Mark the interior of the rectangles
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2
        for row in range(x1 + 1, x2):
            for col in range(y1 + 1, y2):
                grid[row][col] = 0
    
    # Directions for moving in 4 cardinal directions
    dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
    
    # BFS to find the shortest path from character to item
    q = deque([(characterX * 2, characterY * 2, 0)])
    visited = set([(characterX * 2, characterY * 2)])
    
    while q:
        x, y, cnt = q.popleft()
        if (x, y) == (itemX * 2, itemY * 2):
            return cnt // 2  # Since we doubled the grid, divide by 2
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < 102 and 0 <= ny < 102 and (nx, ny) not in visited:
                if grid[nx][ny] == 1:
                    q.append((nx, ny, cnt + 1))
                    visited.add((nx, ny))
    
    return 0  # Shouldn't reach here if the input is valid