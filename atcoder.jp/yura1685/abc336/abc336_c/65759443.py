def gosin(n):
    x = []
    if n == 0:
        return [0]
    sisu = 1
    while n != 0:
        c = n % (5**sisu)
        x.append(c // (5**(sisu-1)))
        n -= c
        sisu += 1
    x.reverse()
    return x

N = int(input())
x5 = gosin(N-1)

d = {0:0, 1:2, 2:4, 3:6, 4:8}
ans = []
for i in x5:
    ans.append(str(d[i]))
print(''.join(ans))