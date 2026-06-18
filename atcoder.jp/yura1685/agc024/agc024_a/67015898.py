A, B, C, K = map(int,input().split())
ans = (A-B)*(-1)**((K%2==0)+1)
print(ans)