H, W, D = map(int,input().split())
S = [input() for _ in range(H)]

yuka = []

for h in range(H):
    for w in range(W):
        if S[h][w] == '.':
            yuka.append((h,w))

n = len(yuka)
ans = 0
for i in range(n-1):
    for j in range(i+1,n):
        h1, w1 = yuka[i]
        h2, w2 = yuka[j]
        m = set()
        for h3, w3 in yuka:
            if abs(h3-h1) + abs(w3-w1) <= D:
                m.add((h3,w3))
            if abs(h3-h2) + abs(w3-w2) <= D:
                m.add((h3,w3))
        ans = max(ans, len(m))

print(ans)