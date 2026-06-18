N = int(input())
A = [0]+list(map(int,input().split()))

now = [0]*(N+1)
for i in range(1,N+1):
    now[A[i]] = i

swap = []

for i in range(1,N+1):
  if A[i] != i:
    ind = now[i] 
    swap.append((i,ind))
    now[i], now[A[i]] = now[A[i]], now[i]
    A[i], A[ind] = A[ind], A[i]

print(len(swap))
for i in swap:
    print(*i)