from collections import deque

def solution(begin, target, words):
    if target not in set(words): return 0
    visited = set()
    queue = deque([(begin,0)])
    while queue:
        word, cnt = queue.popleft()
        if word== target:return cnt
        for w in words:
            dif = 0
            for idx, s in enumerate(word):
                if s != w[idx] : dif += 1
            if dif == 1 and w not in visited:
                queue.append((w,cnt+1))
                visited.add(w)