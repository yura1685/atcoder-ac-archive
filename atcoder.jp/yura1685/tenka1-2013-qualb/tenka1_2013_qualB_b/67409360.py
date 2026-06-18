Q, L = map(int,input().split())

stuck = []
cnt = 0

for _ in range(Q):
    q = input().split()
    if q[0] == 'Push':
        N, M = int(q[1]), int(q[2])
        if cnt + N > L:
            print('FULL')
            exit()
        if stuck:
            n, m = stuck.pop()
            if m == M:
                stuck.append((N+n,M))
            else:
                stuck.append((n,m))
                stuck.append((N,M))
        else:
            stuck.append((N,M))
        cnt += N
    
    if q[0] == 'Pop':
        N = int(q[1])
        if cnt < N:
            print('EMPTY')
            exit()
        X = 0
        while True:
            n, m = stuck.pop()
            if X + n < N:
                X += n
            elif X + n == N:
                break
            else:
                over = X + n - N
                stuck.append((over,m))
                break
        cnt -= N

    if q[0] == 'Top':
        if stuck:
            print(stuck[-1][1])
        else:
            print('EMPTY')
            exit()
    
    if q[0] == 'Size':
        print(cnt)

print('SAFE')