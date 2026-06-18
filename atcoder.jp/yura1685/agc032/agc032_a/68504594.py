N = int(input())
b = [0] + list(map(int,input().split()))

ans = []

for i in range(N+1):
    for j in range(N-i,-1,-1):
        if b[j] == j:
            ans.append(j)
            b.pop(j)
            break

if len(ans) < N+1:
    exit(print(-1))

for i in range(N-1,-1,-1):
    print(ans[i])