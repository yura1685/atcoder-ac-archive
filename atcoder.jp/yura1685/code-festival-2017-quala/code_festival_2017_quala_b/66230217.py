N, M, K = map(int,input().split())

for h in range(N+1):
    for w in range(M+1):
        if M*h + N*w - 2*w*h == K:
            print('Yes')
            exit()
print('No')