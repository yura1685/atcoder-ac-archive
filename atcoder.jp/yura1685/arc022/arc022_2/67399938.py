from collections import defaultdict

N = int(input())
A = list(map(int,input().split()))

l, r = 0, 1

ans = 1
cnt = 1
d = defaultdict(int)
d[A[0]] += 1
while r < N:
    if d[A[r]] == 0:
        d[A[r]] += 1
        cnt += 1
    else:
        while A[l] != A[r]:
            d[A[l]] -= 1
            cnt -= 1
            l += 1
        l += 1
    r += 1
    ans = max(ans,cnt)

print(ans)