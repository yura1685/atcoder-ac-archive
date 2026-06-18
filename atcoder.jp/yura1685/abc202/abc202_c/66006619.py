N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
BCj = [B[C[j]-1] for j in range(N)]

Ac = [0 for _ in range(N+1)]
BCjc = [0 for _ in range(N+1)]

for i in range(N):
    Ac[A[i]] += 1
    BCjc[BCj[i]] += 1

ans = 0
for i in range(1,N+1):
    if Ac[i] != 0 and BCjc[i] != 0:
        ans += Ac[i] * BCjc[i]

print(ans)