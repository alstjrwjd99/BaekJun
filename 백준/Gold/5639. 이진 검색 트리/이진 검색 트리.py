import sys
input = sys.stdin.read
sys.setrecursionlimit(10**9)

pre = list(map(int, filter(lambda x: x.strip(), input().split('\n'))))

def post(tree):
    if len(tree) == 0 :
        return
    
    root = tree[0]
    left, right = [] , []
    for i in range(1, len(tree)) :
        if tree[i] > root :
            left = tree[1:i]
            right = tree[i:]
            break
    else:
        left = tree[1:]
    post(left)
    post(right)    
    print(root)

post(pre)