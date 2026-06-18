N, K = map(int,input().split())

up = []
last = 0
cnt = 0
for _ in range(N):
    A = int(input())
    if A > last:
        cnt += 1
    else:
        up.append(cnt)
        cnt = 1
    last = A
if cnt > 1:
    up.append(cnt)

ans = 0
for x in up:
    if x >= K:
        ans += x-K+1

print(ans)