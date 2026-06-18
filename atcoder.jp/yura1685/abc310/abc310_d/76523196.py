from math import factorial

I = input().split()
N, T, M = int(I[0]), int(I[1]), int(I[2])
bad = [[] for _ in range(N)]
for _ in range(M):
    I = input().split()
    a, b = int(I[0]), int(I[1])
    a, b = a-1, b-1
    bad[a].append(b)
    bad[b].append(a)

ans = 0

def dfs(now, ls):
    global ans

    if now == N:
        if len(ls) == T:
            ans += 1
        return 
    
    for s in ls:
        for b in bad[now]:
            if b in s:
                break
        else:
            s.add(now)
            dfs(now + 1, ls)
            s.discard(now)

    if len(ls) < T:
        ls.append(set([now]))
        dfs(now + 1, ls)
        ls.pop()

dfs(0, [])
print(ans)