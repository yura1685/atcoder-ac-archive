def solve():
    N, W = map(int,input().split())
    C = list(map(int,input().split()))
    W2 = W * 2
    L = [0] * W2
    for i in range(N):
        L[i % W2] += C[i]
    S = sum(L[:W])
    ans = S
    for i in range(W2):
        S -= L[i]
        S += L[(i+W) % W2]
        ans = min(ans, S)
    print(ans)

T = int(input())
for _ in range(T):
    solve()