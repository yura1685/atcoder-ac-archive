N = int(input())
A = list(map(int,input().split()))
M = max(A)
P = [0]*(M+1)
for a in A:
    P[a] += 1

for p in range(1,M+1):
    if P[p] == 0:
        continue
    if P[p] > 1:
        P[p] = 0
    for j in range(p*2,M+1,p):
        P[j] = 0

print(sum(P))