from collections import defaultdict

def hoge(X: list) -> int:
    n = len(X)
    if n == 0: return 0
    s_sum = sum(X)
    res = (n+1) * s_sum // 2

    for k in range(2, 26):
        powk = 1 << k    
        ck = 0
        dd = {}
        dc = {}
        for x in X:
            y = x % powk
            target = (powk - y) % powk
            if target in dd:
                ck += dd[target] + dc[target] * x
            dd[y] = dd.get(y, 0) + x
            dc[y] = dc.get(y, 0) + 1
    
        res -= ck // powk
    return res

d = defaultdict(list)
d_sum = defaultdict(int)
N = int(input())
A = list(map(int, input().split()))
for a in A:
    cnt = 0
    while a % 2 == 0:
        a //= 2
        cnt += 1
    d[cnt].append(a)

keys = sorted(d.keys())

for key in keys:
    d_sum[key] = sum(d[key])

ans = 0

for L in d.values():
    ans += hoge(L)

for u in keys:
    for v in keys:
        if u >= v:
            continue
        ans += d_sum[u] * len(d[v]) + pow(2, v-u) * d_sum[v] * len(d[u])

print(ans)