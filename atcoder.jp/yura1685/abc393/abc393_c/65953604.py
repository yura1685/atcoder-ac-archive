N, M = map(int,input().split())
ans = 0
d = []

for _ in range(M):
    u, v = map(int,input().split())
    if u == v:
        ans += 1
    else:
        u, v = max(u,v), min(u,v)
        d.append((u,v))
ans += len(d) - len(set(d))
print(ans)