from collections import deque

N = int(input())
mod = 10 ** 9 + 7
g = [[] for _ in range(N)]
for _ in range(N-1):
    u, v, w = map(int, input().split())
    g[u-1].append((v-1, w))
    g[v-1].append((u-1, w))

xor = [0] + [-1] * (N-1)

dq = deque([0])
while dq:
    u = dq.popleft()
    for v, w in g[u]:
        if xor[v] >= 0:
            continue
        xor[v] = xor[u] ^ w
        dq.append(v)

ans = 0
for bit in range(60):
    c0, c1 = 0, 0
    for x in xor:
        if (x >> bit) & 1:
            c1 += 1
        else:
            c0 += 1
    ans += c0 * c1 * pow(2, bit, mod)
    ans %= mod

print(ans)