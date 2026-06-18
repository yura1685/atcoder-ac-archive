N, M = map(int,input().split())
A = [int(input()) for _ in range(M)]
A.reverse()

c = [0]*(N+1)
ans = []
for a in A:
    if c[a] == 0:
        c[a] = 1
        print(a)
        
for i in range(1,N+1):
    if c[i] == 0:
        print(i)