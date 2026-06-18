N, Q = map(int,input().split())
glid = []
for _ in range(N):
    x = list(map(int,input().split()))
    glid.append(x[1:])
for q in range(Q):
    s, t = map(int,input().split())
    print(glid[s-1][t-1])