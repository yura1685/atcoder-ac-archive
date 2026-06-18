N = int(input())
M, T = [], []
for i in range(N):
    man, time = map(int,input().split())
    M.append(man)
    T.append(time)

ans = 0

for start in range(24):
    U = []
    attend = 0
    for j in range(N):
        U.append((T[j] + start)%24)
        if 9 <= U[j] <= 17:
            attend += M[j]
    ans = max(ans, attend)
print(ans)