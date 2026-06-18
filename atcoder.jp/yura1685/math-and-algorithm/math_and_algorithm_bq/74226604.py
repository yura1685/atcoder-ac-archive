N = int(input())
mod = 10 ** 9 + 7
ans = N * (N + 1) * pow(2, mod-2, mod)
print(ans * ans % mod)