N, K = map(int,input().split())
A = list(map(int,input().split()))
h = [(A[i],i) for i in range(N)]
h.sort()

snack = [K//N]*N
K %= N
for i in range(K):
    a, x = h[i]
    snack[x] += 1

for i in snack:
    print(i)