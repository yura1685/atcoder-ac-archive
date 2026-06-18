N, L = map(int,input().split())
allapple = 0
for i in range(1,N+1):
    allapple += L+i-1
minapple = 100000
for i in range(1,N+1):
    if minapple > abs(L+i-1):
        minapple = abs(L+i-1)
        ans = L+i-1

print(allapple - ans)