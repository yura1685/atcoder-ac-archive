def solve():
    N = int(input())
    P = list(map(int, input().split()))
    ans = int(P == list(range(1, N+1)))
    mod = 998244353
    for i in range(N):
        if P[i] != i + 1:
            break
        ans += N - i - 1
        if ans >= mod: ans %= mod
    print(ans)

for _ in range(int(input())):
    solve()