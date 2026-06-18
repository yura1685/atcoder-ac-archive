from collections import deque

def f(X):
    res = 0
    for c in X:
        if 'A' <= c <= 'Z':
            v = ord(c) - ord('A')
        else:
            v = ord(c) - ord('a') + 26
        res = res * 52 + v
    return res

N = int(input())
g = [[] for _ in range(140608)]
rev_g = [[] for _ in range(140608)]
S = [input() for _ in range(N)]
for s in S:
    fr, to = s[:3], s[-3:]
    g[f(fr)].append(f(to))
    rev_g[f(to)].append(f(fr))

deg = [len(g[i]) for i in range(140608)]
# 0: 引き分け，1: 勝ち，-1: 負け
ans = [0] * 140608
dq = deque()

for i in range(140608):
    if deg[i] == 0:
        ans[i] = -1
        dq.append(i)

while dq:
    v = dq.popleft()
    for u in rev_g[v]:
        if ans[u] != 0:
            continue
        if ans[v] == -1:
            ans[u] = 1
            dq.append(u)
        elif ans[v] == 1:
            deg[u] -= 1
            if deg[u] == 0:
                ans[u] -= 1
                dq.append(u)

for s in S:
    res = ans[f(s[-3:])]
    print('Takahashi' if res == -1 else 'Aoki' if res == 1 else 'Draw')