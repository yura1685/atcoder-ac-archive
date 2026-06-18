import bisect

N = int(input())
A = list(map(int,input().split()))

S = sum(A)
A += A

s = 0; L = []
for i in range(2*N):
    s += A[i]
    L.append(s)

for i in range(N):
    want = L[i] + S/10
    if bisect.bisect(L,want) - bisect.bisect_left(L,want) != 0:
        print('Yes')
        exit()
print('No')    