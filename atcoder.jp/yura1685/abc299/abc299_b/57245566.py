N, T = map(int,input().split())
C = list(map(int,input().split()))
R = list(map(int,input().split()))
ans = 0
if C.count(T) == 0:
    T = C[0]
for i in range(N):
    if C[i] == T:
        ans = max(ans,R[i])
print(R.index(ans)+1)