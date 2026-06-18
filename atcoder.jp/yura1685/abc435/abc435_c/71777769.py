N = int(input())
A = list(map(int,input().split()))

a = 0
for i in range(N):
    a = max(a,A[i])
    a -= 1
    if a == 0:
        exit(print(i+1))

print(N)