import heapq

def solve():
    N, K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = sorted((A[i], B[i]) for i in range(N))
    hq = [-C[i][1] for i in range(K)]
    S = -sum(hq)
    heapq.heapify(hq)
    ans = C[K-1][0] * S
    for i in range(K,N):
        n = heapq.heappop(hq)
        S += n + C[i][1]
        heapq.heappush(hq, -C[i][1])
        ans = min(ans, C[i][0]*S)
    print(ans)

for _ in range(int(input())):
    solve()