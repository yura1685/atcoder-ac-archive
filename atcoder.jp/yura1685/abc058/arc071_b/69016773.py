n, m = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
mod = 10**9 + 7

X = sum((-n+2*i+1)*x[i] for i in range(n))
Y = sum((-m+2*i+1)*y[i] for i in range(m))

print(X*Y%mod)