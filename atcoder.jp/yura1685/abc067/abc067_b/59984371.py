N, K = map(int,input().split())
l = list(map(int,input().split()))
L = sorted(l, reverse = True)
print(sum(L[:K]))