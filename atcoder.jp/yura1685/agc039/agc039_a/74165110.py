from more_itertools import run_length

S = list(run_length.encode(input()))
K = int(input())

if len(S) == 1: exit(print(S[0][1] * K // 2))

if S[0][0] != S[-1][0]:
    ans = 0
    for s, c in S:
        ans += c // 2
    print(ans * K)

else:
    N = len(S)
    ans = 0
    for i in range(1, N-1):
        ans += S[i][1] // 2
    ans *= K
    a, b = S[0][1], S[-1][1]
    ans += a // 2 + (a + b) // 2 * (K - 1) + b // 2
    print(ans)