def solve():
    N = int(input())
    C = []
    S = 0
    for _ in range(N):
        W, P = map(int,input().split())
        S += P
        C.append(W+P)
    C.sort()
    cnt = 0
    ans = 0
    for i in range(N):
        c = C[i]
        if cnt + c <= S:
            cnt += c
            ans += 1
        else:
            break
    print(ans)

T = int(input())
for _ in range(T):
    solve()