T, M = map(int,input().split())

comb = [[0]*5001 for _ in range(5001)]
comb[0][0] = 1
for n in range(1,5001):
    comb[n][0] = 1
    for k in range(1,n+1):
        comb[n][k] = (comb[n-1][k-1] + comb[n-1][k]) % M

def solve():
    N = int(input())
    C = list(map(int,input().split()))
    S = sum(C)
    ans = 1
    for i in range(N):
        ans = ans * comb[S][C[i]] % M
        S -= C[i]
    print(ans)

for _ in range(T):
    solve()