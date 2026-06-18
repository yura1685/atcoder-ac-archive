N, K = map(int,input().split())

if K == 1 or K == N:
    hoge = (N-1)*3 + 1
    print(hoge/(N*N*N))
    exit()

hoge = 6*(K-1)*(N-K) + 3*N - 2
print(hoge/(N*N*N))