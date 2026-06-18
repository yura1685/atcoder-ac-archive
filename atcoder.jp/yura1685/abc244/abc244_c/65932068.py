N = int(input())
x = [0]*(2*N+1)
for _ in range(2*N):
    print(x.index(0)+1)
    x[x.index(0)] += 1
    aoki = int(input())
    if aoki == 0:
        break
    x[aoki-1] += 1