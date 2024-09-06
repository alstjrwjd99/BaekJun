import sys
input = sys.stdin.readline

S = input().strip()
made = set()

for i in range (1,len(S) + 1):
    for j in range (len(S)-i +1 ):
        made.add(S[j:j+i])

print(len(made))
