N, M = map(int,input().split())

ans = [-1]*N
for _ in range(M):
    s, c = map(int,input().split())
    if ans[s-1] == -1:
        ans[s-1] = c
    elif ans[s-1] != c:
        print(-1)
        exit()
    
if N != 1 and ans[0] == 0:
    print(-1)
    exit()

for i in range(N):
    if ans[i] == -1 and i == 0 and N == 1:
        ans[0] = 0
    elif ans[i] == -1 and i == 0:
        ans[0] = 1
    elif ans[i] == -1:
        ans[i] = 0

x = ''
for i in ans:
    x += str(i)

print(x)