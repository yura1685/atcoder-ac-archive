N, K = map(int,input().split())
V = list(map(int,input().split()))

ans = 0
for a in range(N+1):
    for b in range(N+1):
        if a + b > min(N,K):
            break
        L = V[:a] + V[N-b:]
        L.sort(reverse=True)
        left = K - a - b
        while L and L[-1] < 0 and left > 0:
            L.pop()
            left -= 1
        ans = max(ans,sum(L))

print(ans)