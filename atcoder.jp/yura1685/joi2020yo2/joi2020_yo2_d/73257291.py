from collections import deque

g = [[1],[0,2,4],[1,3,5],[2,6],[1,5,7],[2,4,6,8],
     [3,5,9],[4,8],[5,7,9],[6,8]]

M, R = map(int,input().split())
check = [-1] * (10*M)
check[0] = 0
dq = deque([(0,0)])

while dq:
    r, u = dq.popleft()
    n = 10*r + u
    step = check[n]
    
    r2 = n % M
    if r2 == R:
        exit(print(step+1))
    
    n2 = 10*r2 + u
    if check[n2] == -1:
        check[n2] = step + 1
        dq.append((r2, u))

    for v in g[u]:
        n3 = 10 * r + v
        if check[n3] == -1:
            check[n3] = step + 1
            dq.append((r, v))