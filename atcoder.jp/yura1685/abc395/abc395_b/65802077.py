N = int(input())
glid = [['.']*N for _ in range(N)]
x = '#.'
for i in range(1,N+1):
    j = N+1-i
    if i <= j:
        for h in range(i-1,j):
            for w in range(i-1,j):
                glid[h][w] = x[i%2==0]
for i in glid:
    print(''.join(i))