N, K = map(int,input().split())
if K > (N-1)*(N-2)//2: exit(print(-1))
print(N-1-K + (N-1)*(N-2)//2)
for i in range(2,N+1):
    print(1,i)

K = -K + (N-1)*(N-2)//2
L = []
for i in range(2,N):
    for j in range(i+1,N+1):
        L.append((i,j))

while K:
    i, j = L.pop()
    print(i,j)
    K -= 1