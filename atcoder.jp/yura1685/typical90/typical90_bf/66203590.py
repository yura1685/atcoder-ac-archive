def f(x):
    ans = 0
    for i in str(x):
        ans += int(i)
    return ans

M, K = map(int,input().split())
N = M
hoge = [-1]*100000
hoge[N] = 0

for i in range(1,K+1):
    N += f(N)
    N %= 100000
    if hoge[N] != -1:
        shuki = i - hoge[N]
        t = i
        break
    else:
        hoge[N] = i
else:
    print(N)
    exit()


if K > t:
    K = (K-t)%shuki + t

for _ in range(K):
    M += f(M)
    M %= 100000

print(M)