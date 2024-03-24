import sys
input = sys.stdin.readline

stack1 = list(input().strip())
stack2 = []

n = int(input().strip())

for _ in range(n):
    m = input().strip()
    if "L" in m:
        if stack1:
             stack2.append(stack1.pop())
    elif "D" in m:
        if stack2:
            stack1.append(stack2.pop())                        
    elif "B" in m:
        if stack1:
            stack1.pop()
    else:
        stack1.append(m[2])

stack2 = reversed(stack2)
print(*stack1, *stack2, sep="")