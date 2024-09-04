import sys
input = sys.stdin.readline

names = ['Inseo', 'Junsuk', 'Jungwoo', 'Jinwoo', 'Youngki']

difficulty = [ list(map(int,input().split())) for _ in range (5)]
process_time = [ list(map(int,input().split())) for _ in range (5)]
expected = [0] * 5

for x in range (5):
    for y in range (5):
        for i in range (5):
            expected[x] += difficulty[x][i] * process_time[i][y]

idx = 0
for i in range (5):
    if expected[i] <= expected[idx]:
        idx = i
print(names[idx])