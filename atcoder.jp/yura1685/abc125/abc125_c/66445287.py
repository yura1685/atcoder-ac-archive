from math import gcd

N = int(input())
A = list(map(int,input().split()))

gl = [A[0]]
gr = [A[-1]]

for i in range(N-1):
    gl.append(gcd(gl[i],A[i+1]))
    gr.append(gcd(gr[i],A[N-i-2]))
gr.reverse()

ans = 0
for i in range(N):
    if i == 0:
        g = gr[1]
    elif i == N-1:
        g = gl[N-2]
    else:
        g = gcd(gl[i-1],gr[i+1])
    ans = max(ans, g)

print(ans)