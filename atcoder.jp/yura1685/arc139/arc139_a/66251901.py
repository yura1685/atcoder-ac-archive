N = int(input())
T = list(map(int,input().split()))

A = []
for i in range(N):
    t = T[i]
    base = 2**t
    if A == []:
        A.append(base)
        continue
    c = A[-1]
    if c < base:
        A.append(base)
        continue
    if c % base == 0:
        n = c // base
        if n % 2 == 0:
            n += 1
        else:
            n += 2
        A.append(base*n)
        continue
    n = int(c//base)+1
    if n % 2 == 0:
        n += 1
    A.append(n*base)

print(A[-1])