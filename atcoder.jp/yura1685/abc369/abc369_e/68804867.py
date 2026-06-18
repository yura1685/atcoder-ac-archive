from itertools import product, permutations

N, M = map(int,input().split())
q = []
INF = float('inf')
d = [[0 if i == j else INF for j in range(N)] for i in range(N)]

for i in range(M):
    U, V, T = map(int,input().split())
    U, V = U-1, V-1
    q.append((U,V,T))
    d[U][V] = d[V][U] = min(d[U][V], T)

for k in range(N):
    for i in range(N):
        for j in range(N):
            d[i][j] = min(d[i][j], d[i][k]+d[k][j])

Q = int(input())
for _ in range(Q):
    K = int(input())
    B = [int(i)-1 for i in input().split()]
    A = [[(q[b][0],q[b][1]),(q[b][1],q[b][0])] for b in B]
    ans = INF
    S = sum(q[b][2] for b in B)
    for P in product(*A):
        for p in permutations(P):
            R = d[0][p[0][0]] + d[p[-1][-1]][-1]
            for i in range(K-1):
                R += d[p[i][1]][p[i+1][0]]
            ans = min(ans,R)
    print(ans + S)
