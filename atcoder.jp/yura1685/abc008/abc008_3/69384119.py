from math import comb, factorial

N = int(input())
C = [int(input()) for _ in range(N)]
A = [0] * N

for i in range(N):
    cnt = 0
    for j in range(N):
        if C[i] % C[j] == 0:
            cnt += 1
    A[i] = cnt - 1

ans = 0
for a in A:
    for i in range(0,a+1,2):
        for j in range(N-a):
            ans += comb(a,i) * comb(N-a-1,j) * factorial(i+j) * factorial(N-i-j-1)

# 流石に100!はでかすぎるか...。
print(ans/factorial(N))