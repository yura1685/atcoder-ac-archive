A, B, C = [int(input()) for _ in range(3)]
mod = 10**9 + 7
y = B * (A-C) * pow(B*C - A*B - A*C, mod-2, mod) % mod
x = (B-A) * (y + 1) * pow(A, mod-2, mod) % mod
print(x, y)