# 입력
import sys
input = sys.stdin.readline
N,L = map(int,input().split())
maps = []
for _ in range (N):
    maps.append(list(map(int,input().split())))

answer = 0
# 지도를 순회하며 내림차순인 경우 or 오름차순(반대에서 건너는 경우)인 경우만 건너갈 수 있음
# 그 중 경사로를 설치하려면 높이 차이가 1이 나면서 여유 공간 L 만큼이 있어야함
def line_check(line) :
    for i in range (1,N):
        # 차이가 -1, 0, 1 중 하나가 아니면 안됨
        if abs(line[i] - line[i-1]) > 1:
            return False
        if line[i] < line[i-1] :
            for k in range(L): 
                # 범위 넘어감 or 이미 설치함 or 낮은 곳의 높이가 다른 경우, 그만  
                if i + k >= N or used[i + k] or line[i] != line[i + k]:
                    return False
                # 높이가 같은 경우 사용으로 체크 
                if line[i] == line[i + k]:   
                    used[i + k] = True
        # 현재 > 이전, 경사로를 만들기 위해 왼쪽을 스캔함
        elif line[i] > line[i - 1]:         
            for k in range(L):
                # 범위 넘어감 or 이미 설치함 or 낮은 곳의 높이가 다른 경우, 그만
                if i - k - 1 < 0 or line[i - 1] != line[i - k - 1] or used[i - k - 1]:  
                    return False
                # 높이가 같은 경우 사용 여부 체크 
                if line[i - 1] == line[i - k - 1]:   
                     used[i - k - 1] = True
    return True
        
# 가로 탐색
for x in range (N):
    used = [False for _ in range (N)]
    if line_check(maps[x]):
        answer += 1
    
# 세로 탐색
for x in range (N):
    used = [False for _ in range (N)]
    if line_check([maps[i][x] for i in range (N)]):
        answer += 1

print(answer)