from itertools import combinations

N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
if K < N - K:
    for picka in combinations(A, K):
        xor = 0
        for a in picka:
            xor ^= a
        ans = max(ans, xor)

else:
    XOR = 0
    for a in A:
        XOR ^= a
    for picka in combinations(A, N - K):
        xor = XOR
        for a in picka:
            xor ^= a 
        ans = max(ans, xor)

print(ans)