from math import gcd
N, M = map(int, input().split())
S, T = input(), input()
if N < M:N, M, S, T = M, N, T, S
if S[0] != T[0]: exit(print(-1))
G = gcd(N, M)
if G == 1: exit(print(N*M))
if S[::N//G] == T[::M//G]: print(N*M//G)
else: print(-1)