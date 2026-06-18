N = int(input())

P = [0,1] + [2]*(N-1)

for i in range(2,N+1):
    p = P[i]
    for j in range(2*i,N+1,i):
        P[j] = p+1

print(*P[1:N+1])