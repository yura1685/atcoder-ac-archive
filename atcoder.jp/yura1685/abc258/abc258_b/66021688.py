N = int(input())
A = [list(input()) for _ in range(N)]
B = [A[i]*3 for i in range(N)]
B = B*3

c = [(-1,-1),(-1,0),(-1,1),
     ( 0,-1),       ( 0,1),
     ( 1,-1),( 1,0),( 1,1)]

ans = []
for h in range(N):
    for w in range(N):
        for dh, dw in c:
            x = B[h+N][w+N]
            for i in range(1,N):
                x += B[h+N+dh*i][w+N+dw*i]
            ans.append(int(x))

ans.sort(reverse=True)
print(ans[0])
