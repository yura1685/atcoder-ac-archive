from sortedcontainers import SortedList

H, W, X = map(int,input().split())
P, Q = map(int,input().split())
INF = float('INF')
S = ([[INF]*(W+2)] +
    [[INF]+list(map(int,input().split()))+[INF] for _ in range(H)] +
    [[INF]*(W+2)])

M = SortedList([(S[P-1][Q],P-1,Q),
                (S[P][Q-1],P,Q-1),
                (S[P][Q+1],P,Q+1),
                (S[P+1][Q],P+1,Q)])

c = [(-1,0),(0,-1),(0,1),(1,0)]
check = [[0]*(W+2) for _ in range(H+2)]
check[P][Q] = 1
for dh, dw in c:
    check[P+dh][Q+dw] = 1
T = S[P][Q]

while M:
    size, h, w = M.pop(0)
    if T <= size * X:
        break
    T += size
    for dh, dw in c:
        if check[h+dh][w+dw] == 0:
            check[h+dh][w+dw] = 1
            M.add((S[h+dh][w+dw], h+dh, w+dw))

print(T)