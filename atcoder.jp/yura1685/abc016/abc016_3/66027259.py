N, M = map(int,input().split())

friend = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int,input().split())
    friend[a].append(b)
    friend[b].append(a)

for u in range(1, N+1):
    my_friends = set(friend[u])
    c = set()
    for f in my_friends:
        c.update(friend[f])
    c.discard(u)
    ans = len(c - my_friends)
    print(ans)