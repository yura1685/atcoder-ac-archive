N, M = map(int, input().split())
S = set()
for _ in range(M):
    A, B, C = map(int, input().split())
    A, B, C = A-1, B-1, C-1
    X = (1 << A) + (1 << B) + (1 << C)
    S.add(X)

ans = 0
for med in range(1 << N):
    for s in S:
        if (s & med) == s:
            break
    else:
        cnt = 0
        for bit in range(N):
            if med & (1 << bit):
                pass
            med ^= 1 << bit
            for s in S:
                if (s & med) == s:
                    cnt += 1
                    break
            med ^= 1 << bit
        ans = max(ans, cnt)

print(ans)