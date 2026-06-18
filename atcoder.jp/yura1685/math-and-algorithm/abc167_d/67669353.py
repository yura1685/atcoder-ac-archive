N, K = map(int,input().split())
A = [0] + list(map(int,input().split()))
B = [-1]*(N+1)
B[0] = 0
cur = 1
roop = False
while K > 0:
    nx = A[cur]
    if B[nx] < 0 or roop:
        B[nx] = B[cur] + 1
        K -= 1
    else:
        K -= 1
        cyc = B[cur] + 1 - B[nx]
        K %= cyc
        roop = True
    cur = nx
print(cur)