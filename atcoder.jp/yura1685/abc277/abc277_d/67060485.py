N, M = map(int,input().split())
A = list(map(int,input().split()))
A.sort()

if N == 1:
    print(0)
    exit()

ren = []
now = []
for i in range(N-1):
    now.append(A[i])
    if A[i] + 1 >= A[i+1]:
        pass
    else:
        ren.append(now)
        now = []
    if i == N-2:
        now.append(A[N-1])
        ren.append(now)
if A[0] == 0 and A[-1] == M-1 and len(ren) != 1:
    ren[0] += ren[-1]
    ren.pop()

ans = 0
for R in ren:
    ans = max(ans,sum(R))
print(sum(A)-ans)