N = int(input())
K = list(map(int,input().split()))
K = [K[0]] + K + [K[-1]]

L = [1]*N
for i in range(N):
    L[i] = min(K[i],K[i+1])

print(*L)