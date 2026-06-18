import math

N = int(input())
A = list(map(int,input().split()))
ans = 0
gcd = A[0]

for i in range(N):
    gcd = math.gcd(gcd,A[i])

while gcd % 2 == 0:
    ans += 1
    gcd /= 2

print(ans)