import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [[0] * (M) for _ in range (N)]
blocks = []

for _ in range (K):
    h, w = map(int, input().split())
    blocks.append([list(map(int, input().split())) for _ in range (h)])

def rotate(block):
    n = len(block)
    m = len(block[0])
    copy = [[0] * n for _ in range (m)]
    for i in range (n):
        for j in range (m):
            copy[j][n-1-i] = block[i][j]
    return copy

def is_available(block):
    n = len(block)
    m = len(block[0])
    for i in range (N - n + 1):
        for j in range (M - m + 1):
            cant = False
            for a in range (n):
                for b in range (m):
                    if board[i + a][j + b] == 1 and block[a][b] == 1 :
                        cant = True
                        break
            if not cant :
                return True, i ,j 
    return False, 0,0 

def stick_to_note_book(block, first_x, first_y):
    n = len(block)
    m = len(block[0])
    for i in range (n):
        for j in range (m):
            if block[i][j] == 1 :
                board[first_x + i][first_y + j] = 1

for block in blocks:
    target_block = block
    for i in range (4):
        if i != 0 :
            target_block = rotate(target_block)
        can_stick, first_x, first_y = is_available(target_block)
        if can_stick:
            stick_to_note_book(target_block, first_x, first_y)
            break

answer = 0
for i in range (N):
    for j in range (M):
        if board[i][j] == 1 :
            answer += 1
            
print(answer)
    