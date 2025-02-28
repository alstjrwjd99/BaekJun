import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())
# board는 0, 1로 구성: 1이면 비숍을 놓을 수 있는 칸
board = [list(map(int, input().split())) for _ in range(n)]

# 흑/백 칸 분리: 체스판의 색상 분할을 이용 (i+j의 홀짝)
black_positions = []
white_positions = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:  # 1인 칸에만 비숍을 놓을 수 있음
            if (i + j) % 2 == 0:
                black_positions.append((i, j))
            else:
                white_positions.append((i, j))

# 대각선 체크 배열: 우상향 대각선 (i+j), 우하향 대각선 (i-j+n-1)
d1 = [False] * (2 * n - 1)  # 우상향
d2 = [False] * (2 * n - 1)  # 우하향

# 각 그룹에서 놓을 수 있는 최대 비숍 개수를 저장할 변수 (리스트로 감싸서 mutable하게 사용)
best_black = [0]
best_white = [0]

def backtrack(positions, idx, count, best):
    # 가지치기: 남은 칸 수를 더해도 현재 최댓값(best[0])을 넘지 못하면 종료
    if count + len(positions) - idx <= best[0]:
        return
    if idx >= len(positions):
        best[0] = max(best[0], count)
        return

    # 현재 칸을 건너뛰는 경우
    backtrack(positions, idx + 1, count, best)
    
    r, c = positions[idx]
    d1_idx = r + c
    d2_idx = r - c + n - 1
    if not d1[d1_idx] and not d2[d2_idx]:
        d1[d1_idx] = True
        d2[d2_idx] = True
        backtrack(positions, idx + 1, count + 1, best)
        d1[d1_idx] = False
        d2[d2_idx] = False

# 흑색 칸과 백색 칸은 서로 독립적이므로 각각 백트래킹 수행
backtrack(black_positions, 0, 0, best_black)
backtrack(white_positions, 0, 0, best_white)

print(best_black[0] + best_white[0])