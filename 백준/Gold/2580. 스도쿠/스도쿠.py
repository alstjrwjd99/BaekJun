import sys
input = sys.stdin.readline

# 9x9 스도쿠 보드 입력 받기
board = [list(map(int, input().split())) for _ in range(9)]

def find_empty():
    """빈 칸(0)을 찾는 함수, 없으면 (-1, -1)을 반환"""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return -1, -1

def is_valid(num, row, col):
    """해당 숫자가 현재 위치에 유효한지 확인하는 함수"""
    # 가로 검사
    if num in board[row]:
        return False
    
    # 세로 검사
    if num in [board[i][col] for i in range(9)]:
        return False
    
    # 3x3 정사각형 검사
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    
    return True

def dfs():
    """스도쿠를 해결하는 재귀 함수"""
    row, col = find_empty()
    
    # 더 이상 빈 칸이 없으면, 모든 칸이 채워졌다는 의미
    if row == -1 and col == -1:
        return True
    
    for num in range(1, 10):
        if is_valid(num, row, col):
            board[row][col] = num
            
            if dfs():  # 다음 빈 칸에 대해 재귀 호출
                return True
            
            board[row][col] = 0  # 실패하면 다시 0으로 되돌림
    
    return False

dfs()

# 결과 출력
for row in board:
    print(' '.join(map(str, row)))