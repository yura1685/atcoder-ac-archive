import heapq

N, M = map(int, input().split())
P = list(map(int, input().split()))
L = list(map(int, input().split()))
D = list(map(int, input().split()))

X = []
for p in P: X.append((p,1,0))
for i in range(M): X.append((L[i], 0, D[i]))
X.sort()

ans = 0
C = []
for p, i, d in X:
    if i == 0:
        heapq.heappush(C, -d)
    else:
        if not C:
            ans += p
        else:
            w = heapq.heappop(C)
            ans += p + w

print(ans)