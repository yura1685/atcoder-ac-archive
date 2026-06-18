from functools import lru_cache

N = int(input())
karuta = [('',-1),('{',-1)]
for i in range(N):
    karuta.append((input(), i))
karuta.sort()

@lru_cache(maxsize=2)
def LCP(S,T):
    n = min(len(S), len(T))
    for i in range(n):
        if S[i] != T[i]:
            return i
    return n

ans = [-1] * N

for i in range(1,N+1):
    S, ind = karuta[i]
    T1, T2 = karuta[i-1][0], karuta[i+1][0]
    ans[ind] = max(LCP(T1,S), LCP(S,T2))

print(*ans, sep='\n')