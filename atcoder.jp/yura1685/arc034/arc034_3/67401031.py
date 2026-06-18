from collections import defaultdict

A, B = map(int,input().split())

# A!/B! の約数の個数を答えれば良いんだよな（岡田斗司夫）
# つまり、(B+1)(B+2)...(A-1)*A

d = defaultdict(int)

def prime(n):
    p = 2
    m = n
    while m != 1:
        if p*p > m:
            d[m] += 1
            break
        if m % p == 0:
            d[p] += 1
            m //= p
        else:
            p += 1
    return d

for i in range(B+1,A+1):
    prime(i)

ans = 1
mod = 10**9 + 7
for p in d:
    ans = (ans*(d[p]+1)) % mod

print(ans)