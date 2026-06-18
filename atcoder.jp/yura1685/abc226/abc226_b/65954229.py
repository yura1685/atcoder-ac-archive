from collections import deque
N = int(input())

d, n = {}, 0
c = []

for _ in range(N):
    A = deque(map(int,input().split()))
    L = A.popleft()
    if d.get(L) == None:
        d[L] = n
        n += 1
        c.append([tuple(A)])
    else:
        c[d[L]].append(tuple(A))

ans = 0
for x in c:
    ans += len(set(x))

print(ans)