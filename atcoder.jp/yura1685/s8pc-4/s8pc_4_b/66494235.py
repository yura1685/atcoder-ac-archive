from itertools import combinations

N, K = map(int,input().split())
H = list(map(int,input().split()))
L = []

for i in combinations(range(N),K):
    l = [0]*N
    for j in i:
        l[j] = 1
    L.append(l)

ans = 10**18
for c in L:
    money = 0
    A = H.copy()
    for i in range(1,N):
        if c[i] == 1:
            if max(A[:i]) >= A[i]:
                n = max(A[:i]) - A[i] + 1
                A[i] += n
                money += n
    ans = min(ans,money)

print(ans)