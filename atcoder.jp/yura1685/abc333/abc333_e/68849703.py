N = int(input())
Q = [tuple(map(int,input().split())) for _ in range(N)]
Q.reverse()

P = []
M = [0] * (N+1)
ans = 0

cnt = 0
for t, x in Q:
    if t == 1:
        if M[x] == 0:
            P.append(0)
            continue
        P.append(1)
        M[x] -= 1
        cnt -= 1
    else:
        M[x] += 1
        cnt += 1
    ans = max(ans,cnt)

P.reverse()
if sum(M) > 0:
    exit(print(-1))
print(ans)
print(*P)