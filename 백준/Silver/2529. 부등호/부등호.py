import sys
input = sys.stdin.readline

N = int(input())
equals = list(input().split())

global answer
answer = []
numbers = [i for i in range(10)]  

def find(made):
    global answer
    
    if len(made) == (N + 1):  
        answer.append("".join(map(str, made)))  
        return
    
    for num in sorted(numbers, reverse=True): 
        if not made or (equals[len(made) - 1] == '<' and made[-1] < num) or (equals[len(made) - 1] == '>' and made[-1] > num):
            numbers.remove(num) 
            find(made + [num])
            numbers.append(num) 
            
find([])

print(answer[0])
print(answer[-1])