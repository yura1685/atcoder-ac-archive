from bisect import bisect

f = [0, 1]
for _ in range(50): f.append(f[-1] + f[-2])

N = int(input())
ans = 0
while N:
    ans += 1
    if N in f:
        N = 0
    else:
        i = bisect(f, N)
        N -= f[i-1]

print(ans)