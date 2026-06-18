from itertools import permutations,product

N = int(input())
c = input()
S = list(product(['A','B','X','Y'],repeat=2))
S = [''.join(s) for s in S]

ans = float('inf')
for i in range(16):
    for j in range(16):
        if i == j:
            continue
        p = c
        p = p.replace(S[i],'R')
        p = p.replace(S[j],'L')
        ans = min(ans,len(p))

print(ans)