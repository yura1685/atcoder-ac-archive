N = int(input())
T = [1-int(x) for x in input()]

xor = 0
c0, c1 = 0, 0

ans = 0
for t in T:
    xor ^= t
    if xor == 1:
        c1 += 1
        ans += c0 + 1
    else:
        c0 += 1
        ans += c1

print(N*(N+1)//2-ans)