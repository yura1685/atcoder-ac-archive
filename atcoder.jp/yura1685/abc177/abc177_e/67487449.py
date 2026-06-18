N = int(input())
A = list(map(int,input().split()))
M = max(A)
B = [0]*(M+1)
for a in A:
    B[a] += 1

prime = [False] + [False] + [True]*(M-1)

if max(A) == 1:
    print('pairwise coprime')
    exit()

X = []
for p in range(M+1):
    if not prime[p]:
        continue
    cnt = 0
    for i in range(p,M+1,p):
        prime[i] = False
        cnt += B[i]
    X.append(cnt)

XM = max(X)
if XM == N:
    print('not coprime')
elif XM > 1:
    print('setwise coprime')
elif XM == 1:
    print('pairwise coprime')