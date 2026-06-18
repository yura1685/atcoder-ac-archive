N, M = map(int,input().split())
win = [set() for _ in range(N)]
for _ in range(M):
    a, b = map(int,input().split())
    win[a-1].add(b)
    for x in win:
        if a in x:
            x.add(b)
            x |= win[b-1]
    win[a-1] |= win[b-1]

for i in range(N):
    if len(win[i]) == N-1:
        print(i+1)
        exit()
print(-1)