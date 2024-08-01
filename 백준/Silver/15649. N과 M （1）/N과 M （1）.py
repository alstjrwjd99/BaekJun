from itertools import permutations
n,m = map(int,input().split())

n_list = [i+1 for i in range(n)]
ans = list(permutations(n_list, m))
for i in ans:
  print(' '.join(map(str, i)))
