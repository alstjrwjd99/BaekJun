import itertools

# 알파벳을 숫자로 변환하는 함수
def convert(c):
    if c.isdigit():
        return int(c)
    else:
        return -1 * (ord(c) - ord('A') + 1)

# 점수를 계산하는 함수
def calculate_score(cycles, grid):
    score = 1
    for cycle in cycles:
        cycle_score = 1
        for (i, j) in cycle:
            cycle_score *= grid[i][j]
        score *= cycle_score
    if len(cycles) % 2 == 0:
        score *= -1
    return score

# 모든 가능한 순열을 생성하여 최대 및 최소 점수를 찾는 함수
def find_scores(N, grid):
    indices = list(range(N))
    min_score, max_score = float('inf'), float('-inf')

    for rows in itertools.permutations(indices):
        cycles = []
        visited = [False] * N
        for i in range(N):
            if not visited[i]:
                cycle = []
                x = i
                while not visited[x]:
                    visited[x] = True
                    cycle.append((x, rows[x]))
                    x = rows[x]
                cycles.append(cycle)

        score = calculate_score(cycles, grid)
        min_score = min(min_score, score)
        max_score = max(max_score, score)

    return min_score, max_score

# 입력 처리 및 함수 호출
def main():
    N = int(input())
    grid = []
    for _ in range(N):
        grid.append([convert(c) for c in input().strip()])

    min_score, max_score = find_scores(N, grid)
    print(min_score)
    print(max_score)
main()