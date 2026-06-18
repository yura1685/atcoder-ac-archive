K, A, B = map(int,input().split())

if A + 2 >= B:
    print(K+1)
    exit()

cookie = 1
cookie += min(A-1,K)
K -= min(A-1,K)

n = K//2
cookie += (B-A)*n
cookie += (K % 2 == 1)

print(cookie)