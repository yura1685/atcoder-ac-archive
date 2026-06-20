from math import gcd

def solve():
    N, S, K = map(int, input().split())
    S = N - S
    g = gcd(N, S, K)
    N, S, K = N // g, S // g, K // g
    try:
        print((pow(K, -1, N) * S) % N)
    except ValueError:
        print(-1)

for _ in range(int(input())):
    solve()