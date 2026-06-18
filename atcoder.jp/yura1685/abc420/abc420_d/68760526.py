from collections import deque

H, W = map(int,input().split())
A = ['#'*(W+2)] + ['#' + input() + '#' for _ in range(H)] + ['#'*(W+2)]
op = [[-1]*(W+2) for _ in range(H+2)]
cl = [[-1]*(W+2) for _ in range(H+2)]

for h in range(H+2):
    for w in range(W+2):
        if A[h][w] == 'S':
            sh, sw = h, w
            break

d = deque(); d.append((sh,sw,1))
op[sh][sw] = 0
c = [(-1,0),(0,-1),(0,1),(1,0)]
ans = []

while d:
    h, w, flag = d.popleft()
    if flag:
        for dh, dw in c:
            h2, w2 = h+dh, w+dw
            if A[h2][w2] in '.o' and op[h2][w2] == -1:
                op[h2][w2] = op[h][w] + 1
                d.append((h2,w2,1))
            if A[h2][w2] == '?' and cl[h2][w2] == -1:
                cl[h2][w2] = op[h][w] + 1
                d.append((h2,w2,0))
            if A[h2][w2] == 'G':
                ans.append(op[h][w]+1)
    else:
        for dh, dw in c:
            h2, w2 = h+dh, w+dw
            if A[h2][w2] in 'S.x' and cl[h2][w2] == -1:
                cl[h2][w2] = cl[h][w] + 1
                d.append((h2,w2,0))
            if A[h2][w2] == '?' and op[h2][w2] == -1:
                op[h2][w2] = cl[h][w] + 1
                d.append((h2,w2,1))
            if A[h2][w2] == 'G':
                ans.append(cl[h][w]+1)

print(min(ans) if ans else -1)