def solution(begin, target, words):
    # 못찾는 경우
    if target not in set(words):
        return 0
    answer = 0
    stack = [(begin,0)]
    visited = set()
    visited.add(begin)
    while stack:
        start,cnt = stack.pop()        
        for word in words:
            if word not in visited:
                wrong_cnt = 0
                is_diff_one = True
                for i,j in zip(start, word):
                    if i != j:
                        wrong_cnt += 1
                    if wrong_cnt > 1:
                        is_diff_one = False
                        break
                if is_diff_one:
                    if word == target:
                        return cnt + 1
                    stack.append((word,cnt + 1))
                    visited.add(word)