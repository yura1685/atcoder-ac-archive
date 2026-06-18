N, L = map(int,input().split())

ans = 0
for _ in range(N):
    c = input().split()
    if c[1] == 'E':
        ans = max(ans,L-int(c[0]))
    else:
        ans = max(ans,int(c[0]))

print(ans)