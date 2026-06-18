from bisect import bisect

N, K, P = map(int, input().split())
A = list(map(int, input().split())) + [P+1] * (40 - N)

A1, A2 = A[:20], A[20:]

def f(L:list):
    res = [[] for _ in range(21)]
    res[0] = [0]
    for n in range(1, 1 << 20):
        s = 0
        for bit in range(20):
            if n >> bit & 1:
                s += L[bit]
        if s <= P:
            res[n.bit_count()].append(s)
    for r in res: r.sort()
    return res

ans = 0
B1, B2 = f(A1), f(A2)
for pick1 in range(max(0, K-20), min(K, 20) + 1):
    pick2 = K - pick1
    for val1 in B1[pick1]:
        ans += bisect(B2[pick2], P - val1)
print(ans)