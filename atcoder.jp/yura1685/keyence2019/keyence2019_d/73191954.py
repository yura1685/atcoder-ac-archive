from sortedcontainers import SortedSet
N, M = map(int,input().split())
A = SortedSet(map(int,input().split()))
B = SortedSet(map(int,input().split()))
mod = 10**9 + 7
NM = N*M

if len(A) < N or len(B) < M:
    exit(print(0))

ans = 1
for n in range(NM,0,-1):
    inA, inB = n in A, n in B
    if inA and inB:
        continue
    elif inA:
        idxb = B.bisect(n)
        ans = ans * (M - idxb) % mod
    elif inB:
        idxa = A.bisect(n)
        ans = ans * (N - idxa) % mod
    else:
        idxa = A.bisect(n)
        idxb = B.bisect(n)
        ans = ans * ((N - idxa) * (M - idxb) - (NM - n)) % mod

print(ans)