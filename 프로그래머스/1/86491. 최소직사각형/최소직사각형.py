def solution(sizes):
    long = 0
    short = 0
    for size in sizes:
        (large,small) = (size[0],size[1]) if size[0] > size[1] else (size[1],size[0])
        long,short = max(long,large),max(short,small)
        
    return long * short