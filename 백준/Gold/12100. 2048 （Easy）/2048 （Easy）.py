import sys
from copy import deepcopy

input = sys.stdin.readline

N = int(input())
board = []
for _ in range (N):
    board.append(list(map(int,input().split())))
      
           
def up(board):
    for j in range(N):
        pointer = 0
        for i in range(1, N):
            # 현재 값이 0이 아닐때
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                # 포인터가 0을 가리키는 경우
                if board[pointer][j] == 0:
                    board[pointer][j] = tmp
                # 포인터와 현재 값이 같은 경우
                elif board[pointer][j] == tmp:
                    board[pointer][j] *= 2
                    pointer += 1
                # 포인터와 현재 값이 다른 경우
                else :
                    pointer += 1
                    board[pointer][j] = tmp
    return board
def down(board):
    for j in range(N):
        pointer = N - 1
        for i in range(N - 2, -1, -1):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[pointer][j] == 0:
                    board[pointer][j] = tmp
                elif board[pointer][j]  == tmp:
                    board[pointer][j] *= 2
                    pointer -= 1
                else:
                    pointer -= 1
                    board[pointer][j] = tmp
    return board

def left(board):
    for i in range(N):
        pointer = 0
        for j in range(1,N):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[i][pointer] == 0:
                    board[i][pointer] = tmp
                elif board[i][pointer] == tmp:
                    board[i][pointer] *= 2
                    pointer += 1
                else :
                    pointer +=1
                    board[i][pointer] = tmp
    return board

def right(board):
    for i in range(N):
        pointer = N - 1
        for j in range(N - 2, -1, -1):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[i][pointer] == 0:
                    board[i][pointer] = tmp
                elif board[i][pointer]  == tmp:
                    board[i][pointer] *= 2
                    pointer -= 1
                else:
                    pointer -= 1
                    board[i][pointer] = tmp
    return board

def dfs(board, cnt):
    if cnt == 5:
        # 2차원 배열 요소 중 가장 큰 값 반환
        return max(map(max, board))

    # 상, 하, 좌, 우로 움직여 리턴한 값들 중 가장 큰 값 반환
    # board를 꼭 deepcopy하여 함수를 거친 board값이 다음 함수에 들어가지 못하도록 해주어야 한다.
    return max(dfs(up(deepcopy(board)), cnt + 1), dfs(down(deepcopy(board)), cnt + 1), dfs(left(deepcopy(board)), cnt + 1), dfs(right(deepcopy(board)), cnt + 1))

print(dfs(board, 0))
