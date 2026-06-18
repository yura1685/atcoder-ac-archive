N, W = map(int,input().split())
block = [[] for _ in range(W)]

for i in range(N):
    x, y = map(int,input().split())
    block[x-1].append((y,i))

for i in range(W):
    block[i].sort()

s = min(len(l) for l in block)
kieru = [-1] * N
last = 0

for t in range(s):
    maxh = 0
    for i in range(W):
        h = block[i][t][0]
        if h > maxh:
            maxh = h
    for i in range(W):
        ind = block[i][t][1]
        kieru[ind] = max(last+1, maxh)
    last = max(last+1, maxh)

Q = int(input())
for _ in range(Q):
    t, a = map(int,input().split())
    a -= 1
    print('No' if 0 <= kieru[a] <= t else 'Yes')
    