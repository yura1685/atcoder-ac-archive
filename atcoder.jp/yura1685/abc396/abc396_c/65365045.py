N, M = map(int,input().split())
B = sorted(list(map(int,input().split())),reverse = True)
W = sorted(list(map(int,input().split())),reverse = True)

ans = 0
for i in range(min(N,M)):
    if B[i] >= 0:
        ans += B[i]
        if W[i] >= 0:
            ans += W[i]
    else:
        if B[i] + W[i] >= 0:
            ans += B[i] + W[i]
if N > M:
    for i in range(M,N):
        if B[i] >= 0:
            ans += B[i]
        else:
            break
print(ans)