N, L, W = map(int, input().split())
D = list(map(int, input().split()))
print(sum(1 if abs(d - L) <= W else 0 for d in D))