N = int(input())

P = {}
ans = 0
p = 2
hoge = int(N**(0.5)) + 1
while N != 1:
    if p >= hoge:
        print(ans+1)
        exit()

    if N % p == 0:
        p1 = p
        while N % p1 == 0:
            N //= p1
            p1 *= p
            ans += 1
        while N % p == 0:
            N //= p
    if p >= 3:
        p += 2
    if p == 2:
        p += 1

print(ans)