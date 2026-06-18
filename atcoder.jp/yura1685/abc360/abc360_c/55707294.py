N = int(input())
A = list(map(int,input().split()))
W = list(map(int,input().split()))

weight = [0]*(N+1)
weightmax = [0]*(N+1)

for i in range(N):
    weight[A[i]] += W[i]
    if W[i] > weightmax[A[i]]:
        weightmax[A[i]] = W[i]
print(sum(weight) - sum(weightmax))