N = int(input())
mod = 998244353

U, D = [0]*N, [0]*N
U[0], D[0] = 1, 1
lA, lB = map(int,input().split())

for i in range(1,N):
    A, B = map(int,input().split())
    U[i] = (U[i-1] * (A != lA) + D[i-1] * (A != lB)) % mod
    D[i] = (U[i-1] * (B != lA) + D[i-1] * (B != lB)) % mod
    lA, lB = A, B

print((U[-1] + D[-1]) % mod)