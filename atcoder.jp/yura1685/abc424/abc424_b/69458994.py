N, M, K = map(int,input().split())
ac = [0]*N
ans = []
for _ in range(K):
    A, B = map(int,input().split())
    ac[A-1] += 1
    if ac[A-1] == M:
        ans.append(A)

print(*ans)