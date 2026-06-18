N, T = map(int, input().split())
A = list(map(int, input().split()))
M = [0] * N
M[-1] = A[-1]
for i in reversed(range(N-1)):
    M[i] = max(A[i], M[i+1])
mx, cnt = 0, 0
for i in range(N):
    dif = M[i] - A[i]
    if dif == mx:
        cnt += 1
    elif dif > mx:
        mx = dif
        cnt = 1
print(cnt)