from itertools import permutations

S, K = map(str,input().split())
k = int(K)
L = list(set(permutations(S, len(S))))
L.sort()
i = L[k-1]
print(''.join(i))