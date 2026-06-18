# -----------------------------------------------------------------
# This is yura1685's code
# X = a + b (2 <= X <= 2N)
# Y = c + d (2 <= Y <= 2N)
# であって，X - Y = K なる整数の総数
# X = Y + K
#   = 2 + K, 3 + K, ..., 2N + K
# であり，このうち 2 以上 2N 以下であるもの
# min(X) = max(2,2+K)
# max(X) = min(2N,2N+K)
# の範囲にある整数 X とそれに対する Y を成立させる a,b,c,d を考える
# a + b = C (1 <= a, b <= N)
# となる (a,b) の組は？
# -> C と N との大小を比較して場合分けを行う
# -----------------------------------------------------------------

N, K = map(int,input().split())
m = max(2,2+K)
M = min(2*N,2*N+K)

def f(X):
    if X >= N+1:
        return 2*N - X + 1
    else:
        return X - 1
    
ans = 0
for x in range(m,M+1):
    y = x - K
    ans += f(x)*f(y)

print(ans)