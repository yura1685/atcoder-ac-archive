mod = 998244353

Fib = [1,2]
for i in range(2000010):
    Fib.append((Fib[-1] + Fib[-2]) % mod)
Tfb = [1, 2]
for i in range(1,1000003):
    Tfb.append(Tfb[-1] * Fib[2*i + 1] % mod)

def solve():
    H, W = map(int, input().split())
    m, M = min(H, W), max(H, W)
    print(Tfb[m] ** 2 * pow(Fib[2*m], M-m, mod) % mod)

T = int(input())
for _ in range(T):
    solve()