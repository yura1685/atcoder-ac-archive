import bisect

N = int(input())
L = [tuple(map(int,input().split())) for _ in range(N)]
L.sort()
M = 0

ans = []

A =set()
for a, b in L:
    A.add(a)
A = [0] + sorted(list(A))

for i in range(1,len(A)):
    ans.append((A[i-1],0,A[i],0))
    M += 1

for a, b in L:
    ans.append((a,0,a,b))
    M += 1

print(M)
for l in ans:
    print(*l)