from collections import deque

H, W = map(int,input().split())
A = ["#"*(W+2)] + ["#"+input()+"#" for _ in range(H)] + ["#"*(W+2)]
P = [[0]*(W+2) for _ in range(H+2)]
N = int(input())
for _ in range(N):
    R, C, E = map(int,input().split())
    P[R][C] = E

for h in range(H+2):
    for w in range(W+2):
        if A[h][w] == 'S':
            sh, sw = h, w
        if A[h][w] == 'T':
            gh, gw = h, w

M = [[-1]*(W+2) for _ in range(H+2)]

c = [(-1,0),(0,-1),(1,0),(0,1)]
dq = deque([(sh,sw,0)])

while dq:
    h, w, e = dq.popleft()
    if (h,w) == (gh,gw): exit(print('Yes'))
    if P[h][w]:
        e = max(e, P[h][w])
        P[h][w] = 0
    M[h][w] = e 
    if e == 0: continue
    for dh, dw in c:
        if A[h+dh][w+dw] != '#' and M[h+dh][w+dw] < e - 1:
            M[h+dh][w+dw] = e-1
            dq.append((h+dh, w+dw, e-1))

print('No')