from atcoder.dsu import DSU

N, M = map(int,input().split())
e = []
for _ in range(M):
    A, B = map(int,input().split())
    e.append((min(A,B)-1,max(A,B)-1))
e.sort(reverse=True)

dsu = DSU(N)

ans = [0]

cnt = 0
for i in range(N-1,0,-1):
    s = set()
    while cnt < M and e[cnt][0] == i:
        s.add(dsu.leader(e[cnt][1]))
        dsu.merge(e[cnt][0],e[cnt][1])
        cnt += 1
    ans.append(ans[-1] - len(s) + 1)

for i in range(N):
    print(ans[-i-1])