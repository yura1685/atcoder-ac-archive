N, M = map(int, input().split())
A = list(map(int, input().split()))
combo = []

for _ in range(M):
    B, C, *I = map(int, input().split())
    n = 0
    for i in I:
        n |= (1 << (i - 1))
    combo.append((B, n))

ans = 0
for bit in range(1 << N):
    if bit.bit_count() != 9:
        continue
    res = 0
    for i in range(N):
        if (bit >> i) & 1:
            res += A[i]
    for b, n in combo:
        if (n & bit).bit_count() >= 3:
            res += b 
    ans = max(ans, res)

print(ans)