def matrix_mul(A, B, mod):
    A00 = (A[0][0]*B[0][0] + A[0][1]*B[1][0]) % mod
    A01 = (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % mod
    A10 = (A[1][0]*B[0][0] + A[1][1]*B[1][0]) % mod
    A11 = (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % mod
    return [[A00, A01], [A10, A11]]

def matrix_pow(A, n, mod):
    res = [[1, 0], [0, 1]]
    while n > 0:
        if n % 2 == 1:
            res = matrix_mul(res, A, mod)
        A = matrix_mul(A, A, mod)
        n //= 2
    return res

def get_general_term(n, x, y, a0, mod):
    if n == 1: return a0 % mod
    M = [[x % mod, y % mod], [0, 1]]
    Mn = matrix_pow(M, n-1, mod)
    ans = (Mn[0][0] * a0 + Mn[0][1]) % mod
    return ans

N = int(input())
AL = []
for _ in range(N):
    a, L = map(int,input().split())
    AL.append((a,L))
mod = int(input())

ans = 0
cnt = 0
for a, L in AL[::-1]:
    ans += get_general_term(L, pow(10, len(str(a)), mod), a, a, mod) * pow(10, cnt, mod)
    ans %= mod
    cnt += len(str(a)) * L

print(ans)
