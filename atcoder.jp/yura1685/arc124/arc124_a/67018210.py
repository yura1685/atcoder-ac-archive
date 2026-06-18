N, K = map(int,input().split())
s = set()
h = [-1]*N
for i in range(K):
    c, k = input().split()
    k = int(k)
    h[k-1] = i+1
    if c == 'R':
        s.add(i+1)

mod = 998244353
ans = 1

for i in range(N):
    if h[i] == -1:
        ans *= len(s)
    else:
        if h[i] in s:
            s -= {h[i]}
        else:
            s.add(h[i])
    ans %= mod

print(ans)