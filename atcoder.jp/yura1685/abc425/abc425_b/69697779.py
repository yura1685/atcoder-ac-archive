N = int(input())
A = list(map(int,input().split()))
cnt = [0]*(N+1)
for a in A:
    if a > 0:
        cnt[a] += 1
if max(cnt) > 1:
    exit(print('No'))
print('Yes')
B = [b for b in range(1,N+1) if not cnt[b]]
P = A.copy()
for i in range(N):
    if P[i] == -1:
        b = B.pop()
        P[i] = b

print(*P)