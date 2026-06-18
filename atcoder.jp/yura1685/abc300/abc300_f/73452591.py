from itertools import accumulate

N, M, K = map(int,input().split())
S = input()
L = [0] + [S[i] == 'x' for i in range(N)]
A = list(accumulate(L))
ans = 0

for i in range(1,N+1):
    ok, ng = i, N*M + 1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        cnt = A[-1] * (mid // N) + A[mid % N] - A[i-1]
        if cnt > K:
            ng = mid
        else:
            ok = mid
    ans = max(ans, ok-i+1)

print(ans)