N, M = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
if M == 0:
    print(1)
    exit()
sabun = []
for i in range(M-1):
    s = A[i+1] - A[i] - 1
    if s != 0:
        sabun.append(s)
if A[0] != 1:
    sabun = [A[0]-1] + sabun
if A[-1] != N:
    sabun.append(N-A[-1])
if sabun == []:
    print(0)
    exit()
m = min(sabun)
ans = 0
for a in sabun:
    ans += (a//m) + (a%m!=0)

print(ans)