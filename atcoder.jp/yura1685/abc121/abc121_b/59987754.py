def solve(a,b,c):
    answer = c
    n = len(a)
    for i in range(n):
        answer += a[i]*b[i]
    if answer > 0:
        return 1
    else:
        return 0


N, M, C = map(int,input().split())
B = list(map(int,input().split()))
ans = 0
for case in range(N):
    A = list(map(int,input().split()))
    ans += solve(A,B,C)

print(ans)