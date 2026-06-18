N = int(input())
events = []
for _ in range(N):
    l, r = map(int,input().split())
    events.append((l,0))
    events.append((r,1))
events.sort()
ans, cnt = 0, 0
for _, t in events:
    if t == 0:
        ans += cnt
    else:
        cnt += 1
print(N*(N-1)//2 - ans)