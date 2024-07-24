import sys
input = sys.stdin.readline

N,K = map(int, input().split())

fish_territory = []
originX = []
originY = []
originZ = []

for _ in range (N):
    coor = list(map(int, input().split()))
    originX.append(coor[0])
    originX.append(coor[3])
    originY.append(coor[1])
    originY.append(coor[4])
    originZ.append(coor[2])
    originZ.append(coor[5])
    fish_territory.append(((coor[0],coor[1],coor[2]),(coor[3],coor[4],coor[5])))
    
sortX = sorted(set(originX))
sortY = sorted(set(originY))
sortZ = sorted(set(originZ))

compX = dict()
compY = dict()
compZ = dict()

reverse_compX = dict()
reverse_compY = dict()
reverse_compZ = dict()

for idx,c in enumerate(sortX):
    compX[c] = idx
    reverse_compX[idx] = c
for idx,c in enumerate(sortY):
    compY[c] = idx
    reverse_compY[idx] = c
for idx,c in enumerate(sortZ):
    compZ[c] = idx
    reverse_compZ[idx] = c

fish_comp_territory = []

for s, e in fish_territory:
    x1,y1,d1 = s
    x2,y2,d2 = e
    fish_comp_territory.append(((compX[x1],compY[y1],compZ[d1]), (compX[x2],compY[y2],compZ[d2])))

fish_comp_territory.sort()

prefixSum = [[[0] * (2*N) for _ in range (2*N)] for _ in range (2*N)]
answer = 0

for start, end in fish_comp_territory:
    start_x, start_y, start_d = start
    end_x, end_y, end_d = end
    for x in range(start_x,end_x):
        for y in range(start_y,end_y):
            for d in range(start_d,end_d):
                if prefixSum[x][y][d] ==-1:
                    continue
                if prefixSum[x][y][d]<K:
                    prefixSum[x][y][d]+=1
                if prefixSum[x][y][d] ==K:
                    answer+=(reverse_compX[x+1]-reverse_compX[x])*(reverse_compY[y+1]-reverse_compY[y])*(reverse_compZ[d+1]-reverse_compZ[d])
                    prefixSum[x][y][d] = -1
                
print(answer)