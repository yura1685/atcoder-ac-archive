N, K = map(int,input().split())
D = sorted(map(int,input().split()), reverse=True)
print(sum(D[K:]))