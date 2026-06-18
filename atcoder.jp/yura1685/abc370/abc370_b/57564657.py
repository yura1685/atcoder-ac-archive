N = int(input())
S = ['']*N
for i in range(N):
    S[i] = list(map(int,input().split()))

genso = 1
for h in range(1,N+1):
    p, q = max(genso,h), min(genso,h)
    genso = S[p-1][q-1]

print(genso)