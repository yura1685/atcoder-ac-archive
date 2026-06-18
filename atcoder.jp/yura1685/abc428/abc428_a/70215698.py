S, A, B, X = map(int,input().split())
t = X // (A+B)
ans = S*A*t
X %= (A+B)
ans += S*min(X,A)
print(ans)