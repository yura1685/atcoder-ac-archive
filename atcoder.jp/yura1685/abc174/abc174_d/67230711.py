N = int(input())
S = input()

red = [0]*(N+1)
whi = [0]*(N+1)

for i in range(N):
    whi[i+1] = whi[i] + (S[i]=='W')
    red[i+1] = red[i] + (S[-i-1] == 'R')
red.reverse()

ans = 10**8
for i in range(N+1):
    W = whi[i]
    R = red[i]
    ans = min(ans,W+R-min(R,W))

print(ans)