N = int(input())
if N == 1: exit(print('Yes'))

S1 = [tuple(map(int,input().split())) for _ in range(N)]
T1 = [tuple(map(int,input().split())) for _ in range(N)]
sgx, sgy = sum(S1[i][0] for i in range(N)), sum(S1[i][1] for i in range(N))
tgx, tgy = sum(T1[i][0] for i in range(N)), sum(T1[i][1] for i in range(N))
S = [(x*N-sgx, y*N-sgy) for x, y in S1]
T = [(x*N-tgx, y*N-tgy) for x, y in T1]

s0 = next(p for p in S if p != (0, 0))
ds0 = s0[0]**2 + s0[1]**2

for ti in T:
    if ti == (0, 0): continue
    if ti[0]**2 + ti[1]**2 != ds0: continue
    
    S2 = sorted([(sx*ti[0] - sy*ti[1], sx*ti[1] + sy*ti[0]) for sx, sy in S])
    T2 = sorted([(tx*s0[0] - ty*s0[1], tx*s0[1] + ty*s0[0]) for tx, ty in T])
    
    if S2 == T2:
        exit(print('Yes'))

print('No')