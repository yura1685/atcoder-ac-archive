N, M = map(int,input().split())

A = pow(10,N,M)
B = pow(10,N,M*M)
print((B-A)//M)