N, K = map(int, input().split())
D = list(map(int, input().split()))
print(sum(D) - sum(D[K::K+1]))