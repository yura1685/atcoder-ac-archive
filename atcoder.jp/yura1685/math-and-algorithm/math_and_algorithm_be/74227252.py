from math import lcm

N, K = map(int, input().split())
V = list(map(int, input().split()))
ans = 0
for bit in range(1, 1 << K):
    L = 1
    for k in range(K):
        if bit >> k & 1:
            L = lcm(L, V[k])
    ans += (N // L) * (-1) ** (bit.bit_count() + 1)

print(ans)