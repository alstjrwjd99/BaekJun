def solution(s):
    english = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for idx,e in enumerate(english):
        s = s.replace(e,str(idx))
    return int(s)