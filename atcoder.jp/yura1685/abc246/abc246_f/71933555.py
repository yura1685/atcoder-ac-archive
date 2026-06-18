from itertools import product

N, L = map(int,input().split())
S = [input() for _ in range(N)]
S_bit = []
mod = 998244353

for s in S:
    bit = 0
    for char in s:
        bit |= (1 << (ord(char)-ord('a')))
    S_bit.append(bit)

ans = 0
for i in range(1, 1<<N):
    n = i.bit_count()
    all = (1 << 26) - 1
    for j in range(N):
        if (i >> j) & 1:
            all &= S_bit[j]
    cnt = all.bit_count()
    if n % 2 == 1:
        ans = (ans + pow(cnt, L, mod)) % mod
    else:
        ans = (ans - pow(cnt, L, mod)) % mod

print(ans)