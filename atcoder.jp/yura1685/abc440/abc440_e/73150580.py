from heapq import heappop, heappush
N, K, X = map(int,input().split())
A = sorted(map(int,input().split()), reverse=True)

C = (-A[0]*K, (K,) + (0,) * (N-1))
hq = []
heappush(hq, C)

def f(P):
    res = 0
    for i in range(N):
        res += P[i+1] * A[i]
    return res

s = set([hash(C[1])])

for _ in range(X):
    Y, P = heappop(hq)
    for i in range(N-1):
        if P[i]:
            Q = list(P)
            Q[i] = Q[i] - 1
            Q[i+1] = Q[i+1] + 1
            H = hash(tuple(Q))
            if H not in s:
                s.add(H)
                heappush(hq, (Y+A[i]-A[i+1],Q))
    print(-Y)