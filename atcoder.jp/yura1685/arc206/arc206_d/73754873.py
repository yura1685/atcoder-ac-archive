def solve():
    N, K = map(int,input().split())
    if K >= 2:
        ans = list(range(1,N+1))
        ans = list(range(1,N-K+1)) + list(range(N,N-K,-1))
    elif K:
        if N == 1:
            ans = [1]
        elif N < 5:
            ans = []
        else:
            ans = [4,1,3,5,2] + list(range(6,N+1))
    else:
        if N < 8:
            ans = []
        else:
            ans = [6,5,1,2,7,8,4,3] + list(range(9,N+1))
    if ans: print(*ans)
    else:   print(-1)

for _ in range(int(input())):
    solve()