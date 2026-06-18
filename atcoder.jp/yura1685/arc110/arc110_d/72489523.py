N, M = map(int,input().split())
A = list(map(int,input().split()))
S = sum(A)

mod = 10**9 + 7
X = M + N
Y = S + N

fact = [1] * (Y+1)
for i in range(1,Y+1):
    fact[i] = (fact[i-1] * i) % mod
revfact = [1] * (Y+1)
revfact[Y] = pow(fact[Y],-1,mod)
for i in range(Y-1,0,-1):
    revfact[i] = (revfact[i+1] * (i+1)) % mod

ans = revfact[Y]
for i in range(Y):
    ans = ans *(X-i) % mod

print(ans)