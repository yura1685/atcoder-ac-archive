# def f(S, T):
#     X = []
#     diff = 0
#     for i in range(N):
#         if (S >> i & 1) ^ (T >> i & 1) == 1:
#             X.append((C[i], i))
#             diff += 1
#     X.sort()
#     res = 0
#     for i in range(diff):
#         res += X[i][0] * (diff - i)
#         cnt[X[i][1]] += diff - i
#     return res
#
# ans = 0
# for s in range(1 << N):
#     for t in range(1 << N):
#         if s == t:
#             continue
#         ans += f(s, t)
#
# S = sum(cnt) # = 2 ** (2*N) * N * (N+3) // 8
# print(ans % mod)
# print(C)
# print(cnt)
# print(4 ** N * N*(N+3) // 8)
# print(*[cnt[i] - cnt[i+1] for i in range(N-1)])

N = int(input())
C = sorted(map(int, input().split()), reverse=True)
mod = 10**9 + 7

m = 2 * pow(4, N-1, mod)
d = m // 2
cnt = [m + i*d for i in range(N)]
ans = 0
for i in range(N):
    ans += cnt[i] * C[i]
    ans %= mod

print(ans)