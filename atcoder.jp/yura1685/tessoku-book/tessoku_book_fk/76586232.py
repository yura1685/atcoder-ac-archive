from collections import defaultdict

mod = 10 ** 9 + 7
N, P = map(int, input().split())
A = [int(x) % mod for x in input().split()]
D = defaultdict(int)
ans = 0
for i, a in enumerate(A):
    if a == 0:
        if P == 0:
            ans += i
    else:
        b = pow(a, mod-2, mod) * P % mod
        ans += D[b]
    D[a] += 1

print(ans)