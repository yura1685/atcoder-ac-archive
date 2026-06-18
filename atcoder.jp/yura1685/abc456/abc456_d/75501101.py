S = input()
A, B, C = 0, 0, 0
ans = 0
mod = 998244353

for s in S:
    if s == 'a':
        ans += B + C + 1
        A += B + C + 1
    if s == 'b':
        ans += C + A + 1
        B += C + A + 1
    if s == 'c':
        ans += A + B + 1
        C += A + B + 1
    ans %= mod
    A %= mod
    B %= mod
    C %= mod

print(ans)