N = int(input())
A = list(map(int,input().split()))
L = []
for i in range(N):
    L.append([A[i],i+1])
L.sort()
ans = []
for i in range(N):
    ans.append(L[i][1])

print(*ans)