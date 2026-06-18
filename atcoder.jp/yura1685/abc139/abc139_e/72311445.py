from collections import defaultdict

N = int(input())
g = defaultdict(list)
cnt = defaultdict(int)

for i in range(1,N+1):
    A = list(map(int,input().split()))
    for j in range(N-2):
        m, M = min(i,A[j+1]), max(i,A[j+1])
        g[(min(i, A[j]), max(i,A[j]))].append((m, M))
        cnt[(m,M)] += 1

s = set()
for i in range(1,N):
    for j in range(i+1,N+1):
        if cnt[(i,j)] == 0:
            s.add((i,j))

days = 0
while s:
    days += 1
    new_set = set()
    for m, M in s:
        for nm, nM in g[(m,M)]:
            cnt[(nm, nM)] -= 1
            if cnt[(nm, nM)] == 0:
                new_set.add((nm, nM))
    s = new_set

print(-1 if max(cnt.values()) else days)