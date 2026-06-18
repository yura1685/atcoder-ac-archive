N, K = map(int,input().split())
p = list(map(int,input().split()))
coin = 0
for i in range(K):
    coin += min(p)
    p.remove(min(p))
print(coin)