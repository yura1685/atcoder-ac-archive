N = int(input())
A = list(map(int,input().split()))
l_max = [0]*N
r_max = [0]*N
l_max[0] = A[0]; r_max[N-1] = A[N-1]
for i in range(1,N):
    l_max[i] = max(l_max[i-1], A[i])
    r_max[N-i-1] = max(r_max[N-i], A[N-i-1])

D = int(input())
for _ in range(D):
    L, R = map(int,input().split())
    l, r = 0, 0
    if L > 1:
        l = l_max[L-2]
    if R < N:
        r = r_max[R]
    print(max(l,r))