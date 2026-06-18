N = int(input())
p = list(map(int,input().split()))
Q = ['0']*N
for i in range(N):
    Q[p[i]-1] = str(i+1)
print(*Q)