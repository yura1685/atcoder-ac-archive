N, M = map(int,input().split())
A = list(map(int,input().split()))
A.sort()

s = 0
for i in range(N):
    if s + (N-i)*A[i] > M:
        x = int((M-s)/((N-i)))
        print(x)
        exit()
    s += A[i]

print('infinite')