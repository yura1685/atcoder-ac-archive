N, L = map(int,input().split())
K = int(input())
A = list(map(int,input().split()))

yokan = []
for i in range(N+1):
    if i == 0:
        yokan.append(A[i])
    elif i < N:
        yokan.append(A[i]-A[i-1])
    else:
        yokan.append(L-A[N-1])

def cut(length):
    cnt = 0
    now = 0
    res = []
    while cnt <= N:
        now += yokan[cnt]
        if now >= length:
            res.append(now)
            now = 0
        cnt += 1
    if now != 0 and len(res) < K+1:
        res.append(now)
    return res

le, ri = 1, L
ans = 0
while le <= ri:
    mi = (le+ri)//2
    c = cut(mi)
    if len(c) > K and min(c) >= mi:
        ans = max(ans,min(c))
        le = mi + 1
    else:
        ri = mi - 1

print(ans)
