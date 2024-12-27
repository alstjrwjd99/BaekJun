# 10시 30분 시작

import sys
input = sys.stdin.readline

n = int(input())
students = n ** 2
favor = dict()
for _ in range (students) :
    info = list(map(int, input().split()))
    favor[info[0]] = info[1:]

class_room = [[0] * n for _ in range (n)]

def find_empty_sit(sit, length):
    blank_list = []
    for i in range (length):
        for j in range (length):
            if sit[i][j] == 0: blank_list.append((i,j))
    return blank_list

def in_range (x,y):
    return 0<=x<n and 0<=y<n

dxs, dys = (-1,0,1,0),(0,1,0,-1)

# 1번 조건 
# 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸
def find_near_most_favorite(sit, blank_list, student_friend):
    max_list = []
    max_cnt = -1
    for x,y in blank_list:
        cnt = 0
        for dx, dy in zip(dxs,dys):
            nx , ny = x + dx , y + dy
            if in_range(nx,ny) and sit[nx][ny] in student_friend:
               cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
            max_list = [(x,y)]
        elif cnt == max_cnt:
            max_list.append((x,y))
    return max_list

# 2번 조건
# 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
def find_near_empty(sit, can_sit_list):
    max_list = []
    max_cnt = 0
    for x,y in can_sit_list:
        cnt = 0
        for dx, dy in zip(dxs,dys):
            nx , ny = x + dx , y + dy
            if in_range(nx,ny) and sit[nx][ny] == 0:
               cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
            max_list = [(x,y)]
        elif cnt == max_cnt:
            max_list.append((x,y))      
    return max_list


for key, value in favor.items():
    blank_list = find_empty_sit(class_room, n)
    can_sit_list = find_near_most_favorite(class_room, blank_list, value)
    empty_sit_list = find_near_empty(class_room, can_sit_list)
    if len(empty_sit_list) == 1 :
        class_room[empty_sit_list[0][0]][empty_sit_list[0][1]] = key
    else :
        # 3번 조건
        # 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
        info = sorted(empty_sit_list, key= lambda x : (x[0], x[1]))[0]
        class_room[info[0]][info[1]] = key

satisfy = {
    0 : 0,
    1 : 1,
    2 : 10,
    3 : 100,
    4 : 1000
}

answer = 0
for i in range (n):
    for j in range (n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx , ny = i + dx , j + dy
            if in_range(nx,ny) and class_room[nx][ny] in favor[class_room[i][j]]:
                cnt += 1
        answer += satisfy[cnt]

print(answer)