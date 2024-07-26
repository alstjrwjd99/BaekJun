def solution(cards):
    opened = [False] * len(cards)
    box_group = []
    
    def open_box(cards, idx):
        opened[idx] = True
        tmp = [idx]    
        while True:
            next_open = cards[idx] - 1
            if opened[next_open]:
                break
            opened[next_open] = True
            idx = next_open
            tmp.append(idx)
        box_group.append(tmp)
        
    for i in range (len(cards)):
        if opened[i]:
            continue
        open_box(cards,i)
    
    box_group.sort(key=lambda x : -len(x))
    if len(box_group) == 1:
        return 0
    return len(box_group[0]) * len(box_group[1])
